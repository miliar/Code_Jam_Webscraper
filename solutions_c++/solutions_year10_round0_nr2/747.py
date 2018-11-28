// Minimum Scalar Product.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <afx.h>
#include <map>
#include <vector>
#include <stdlib.h>
#include<iostream>
#include<stdlib.h>
#include<memory.h>
#include<string.h>
#include <algorithm>
#include "QuickSort.hpp"

#define  PRECITION 100  //	�мǣ�#define��sdt���治�ܸ�';'

using namespace std;
template<class T> 
void swap(T & x,T & y){T temp = x; x=y; y=temp;}
class hugeInt{
public:
	char primitive[PRECITION];//�ó�Ա��ֵ Ϊ�˷�ֹ50λ��50λ�ĳ˷����Խ��
    bool isPositive;//���ô��������������Ϊ" "��Ϊ����Ϊ"-"
    int intExpress[PRECITION];//��һ�����ε������������������ֵ
	int length;
public:  	
    hugeInt( char * s)//���캯��
	{
		memset( primitive, 0, sizeof( primitive ) );//���ַ����鸳ֵΪ��
		if(strlen(s)!=0&&s[0]=='-')
		{
			isPositive=false;
			s++;
		}
		else
		{
			isPositive=true;
		}
		strcpy( primitive, s );
		memset( intExpress, 0, sizeof( intExpress ) );
        charArrayToIntArray();
	}
	hugeInt()
	{
		memset(primitive,0,sizeof(primitive));
		memset(intExpress,0,sizeof(intExpress));
		isPositive=true;
		length=1;
	}
	void setPositive(){isPositive=true;}
	void setNegative(){isPositive=false;}
	friend istream &operator>>( istream &, hugeInt & );//���������
	friend ostream &operator<<( ostream &, hugeInt & );//���������
	void setHugeInt( char * s )
	{ 
		strcpy( primitive, s );/*�����Զ���0*/
        charArrayToIntArray();
    }
	void intArrayToCharArray()//�����������int����ת��Ϊ������ַ�����
	{
		int i;
		for( i=PRECITION-1; i>=0; i-- )if( intExpress[ i ]!=0 )break;
		if(i==-1){ length=1; primitive[0]='0'; primitive[1]=0;}
		else{
			primitive[ i+1 ]=0;
            length=i+1;//�����ַ�������ĳ���--�����ַ��������������ⲿ����
            for( int j=0; j<length; j++ )primitive[ j ]=intExpress[ length-1-j ]+'0';
		}
	}
	void charArrayToIntArray()//Ĭ���ɸú��������ַ����ĳ���
	{
		length=strlen(primitive);
		for( int i=0; i<length; i++ )intExpress[ i ]=primitive[ length-1-i ]-'0';
	}
	void intToHugeInt( int p )
	{   
		int temp=p;
		if(p<0)
		{
			temp=-p;
			isPositive=false;
		}
		for( int i=0; i<PRECITION&&temp!=0; i++ ){
			intExpress[i]=temp%10;
			temp=temp/10;
		}
		intArrayToCharArray();
	}
	bool isOutOfArrayBounds()//�ж��Ƿ�߽��洦
	{
		return length>=PRECITION;
	}
	hugeInt  absPlus(hugeInt & h, hugeInt & hug);//�����������ľ���ֵ���
    hugeInt  operator+( hugeInt & hug );//�������ļӷ�
	friend hugeInt operator+( hugeInt aa,int p );//(hugeInt+int)
	friend hugeInt operator+( int p,hugeInt d );//(int+hugeInt)
	hugeInt &operator++();//ǰ�������++
	hugeInt operator++( int );//���������++
    operator int()const;//ǿ������ת��
	hugeInt absMinus(hugeInt & h,hugeInt & hug);//�����������ľ���ֵ���
    hugeInt operator-( hugeInt & hug );//�������ļ���
	bool operator < ( hugeInt & hug) const;
	hugeInt operator*( hugeInt & hug );//�˷�
    friend hugeInt operator*( int p, hugeInt  hug );//�������ĳ˷���int*hugeInt��
	friend hugeInt operator*( hugeInt hug, int p );//�������˷���hugeInt*int��
    hugeInt operator/( hugeInt & hug );//�������ĳ���
	hugeInt operator%( hugeInt & hug );//��������Nģ
	bool isEqualTo( hugeInt & hug);//�Ƚ��Ƿ����
	bool abs_isEqualTo(hugeInt & hug);//�ȽϾ���ֵ�Ƿ����
	bool isNotEqualTo( hugeInt & hug);//�Ƚ��Ƿ����
	bool isZero( );//�жϸ������ǲ���Ϊ��
	bool isGreaterThan( hugeInt & hug );//�Ƚ��Ƿ�M>N
	bool abs_isGreaterThan(hugeInt & hug);//�ȽϾ���ֵ�Ƿ�|M|>|N|
	bool isLessThan( hugeInt & hug );//�Ƚ��Ƿ�M<N
	bool abs_isLessThan(hugeInt & hug);//�Ƚ��Ƿ���M|<|N|
    bool isGreaterThanOrEqualTo( hugeInt & hug );//�Ƚ��Ƿ�M>=N
	bool isLessThanOrEqualTo( hugeInt & hug);//�Ƚ��Ƿ�M<=N
};//�����Ա����
////��Ԫ����
bool hugeInt::operator < ( hugeInt & hug) const
{
	hugeInt temp1 = *this;
	hugeInt temp2;
	temp2 = temp1 - hug;
	if (temp2.isPositive)
	{
		return false;
	}
	return true;
}
hugeInt::operator int( )const//ǿ��ת��
{
	int i,s=0;
	for (i=0;i<length;i++)
	{
		s=s*10+(primitive[i]-'0');
		if(s<0)
		{
			cout<<"������ת��Ϊintʱ���\n";  /*���洦����*/
			return 0;
		}
	}
	return s;
}
hugeInt & hugeInt::operator++()//ǰ�������++
{
	int i=0;
	while(i<length)
	{
		if(intExpress[i]!=9)break;
	}
	if(i==length)
	{
		memset(intExpress,0,sizeof(intExpress));
		intExpress[length]=1;
		intArrayToCharArray();
	}
	else
	{
		intExpress[i]+=1;
		primitive[length-1-i]+=1;
	}
	return *this;
}
hugeInt hugeInt::operator++( int )//���������++
{
	static hugeInt temp=*this;  //��֪�����þ�̬�����Ƿ��ܽ������
	++(*this);
	return temp;
}
istream &operator>>( istream & input, hugeInt & hug )//���������
{
	memset(hug.primitive,0,sizeof(hug.primitive));
	memset(hug.intExpress,0,sizeof(hug.intExpress));
	input>>hug.primitive;
	hug.charArrayToIntArray();
	return input;
}
ostream &operator<<( ostream & output,  hugeInt & hug )//���������
{
	if(!hug.isPositive)output<<'-';//��"����""��ֵ"����ʽ���
	output<<hug.primitive;
	return output;
}
bool hugeInt::isEqualTo( hugeInt & hug )//�Ƚ��Ƿ����
{
	if(isPositive==hug.isPositive)return abs_isEqualTo(hug);
	else return false;
}
bool hugeInt::isZero( )
{
	for ( int i=0; i<PRECITION; i++)
	{
		if ( intExpress[i]!=0 ) return false;
	}
	return true;
}
bool hugeInt::isNotEqualTo( hugeInt & hug )//�Ƚ��Ƿ����
{
	return !isEqualTo( hug );
}
bool hugeInt::isGreaterThan( hugeInt & hug )//�Ƚ��Ƿ�M>N
{
	if(isPositive==true&&hug.isPositive==false)return true;//һ��һ��
	if(isPositive==false&&hug.isPositive==true)return false;//һ��һ��
	if(isPositive==true&&hug.isPositive==true)return abs_isGreaterThan(hug);//��Ϊ����
	else return abs_isLessThan(hug);//��Ϊ����
}
bool hugeInt::abs_isGreaterThan(hugeInt & hug)
{
	int len,itslen;
	len = length;
	itslen = hug.length;
	if( len>itslen )return true;
	if( len<itslen )return false;
	for( int i=0; i < len; i++ )
	{
		if( primitive[i] > hug.primitive[i] )return true;
		if( primitive[i] < hug.primitive[i] )return false;
	}
	return false;//˵���������
}
bool hugeInt::abs_isLessThan(hugeInt & hug)
{
	int len,itslen;
	len = length;
	itslen = hug.length;
	if( len<itslen )return true;
	if( len>itslen )return false;
	for( int i=0; i < len; i++ )
	{
		if( primitive[i] > hug.primitive[i] )return false;
		if( primitive[i] < hug.primitive[i] )return true;
	}
	return false;//˵���������
}
bool hugeInt::abs_isEqualTo(hugeInt & hug)
{
	int len,itslen;
	len = length;
	itslen = hug.length;
	if( len!=itslen )return false;
	for(int i=0;i<len;i++)
		if(primitive[i]!=hug.primitive[i])return false;
	return true;
}
bool  hugeInt::isLessThan( hugeInt & hug )//�Ƚ��Ƿ�M<N
{
	if(isPositive&&!hug.isPositive)return false;
	else if(isPositive&&hug.isPositive)return abs_isLessThan(hug);
	else if(!isPositive&&hug.isPositive)return true;
	else return abs_isGreaterThan(hug);
}
bool hugeInt::isGreaterThanOrEqualTo( hugeInt & hug)//�Ƚ��Ƿ�M>=N
{
	if( isGreaterThan( hug ) || isEqualTo( hug ) )
		return true;
	else 
		return false;
}
bool hugeInt::isLessThanOrEqualTo(hugeInt & hug )//�Ƚ��Ƿ�M<=N
{
	if( isLessThan( hug ) || isEqualTo( hug ) )
		return true;
	else 
		return false;
}
hugeInt  hugeInt::absPlus(hugeInt & h, hugeInt & hug) //�����������ű�־
{
	hugeInt temp;
	int carry=0, i=0;
	for( i=0; i<PRECITION; i++ ) //ʵ��������������Ч��
	{
		int t=h.intExpress[i] + hug.intExpress[i] + carry;
		temp.intExpress[i]=t%10;
		carry=t/10;
	}
	temp.intArrayToCharArray();
	return temp;
}
hugeInt  hugeInt::operator+( hugeInt & hug )////�������ļӷ�
{
	if(isPositive==true&&hug.isPositive==true)return absPlus(*this,hug);//��Ϊ����
	if(isPositive==false&&hug.isPositive==false)return absPlus(*this,hug);//��Ϊ����
	if(isPositive==true&&hug.isPositive==false)
	{
		if(abs_isLessThan(hug))
		{
			hugeInt temp=absMinus(hug,*this);
			temp.isPositive=false;
			return temp;
		}
		return absMinus(*this,hug);//һ��һ��
	}
	else//һ��һ��
	{
		if(abs_isGreaterThan(hug))
		{
			hugeInt temp=absMinus(*this,hug);
			temp.isPositive=false;
			return temp;
		}
		return absMinus(hug,*this);
	}
}
hugeInt operator+( int b, hugeInt hug)
{
	hugeInt temp;
	temp.intToHugeInt(b);
	temp=hug+temp;
	return temp;
}
hugeInt operator+( hugeInt hug,int d )
{
	hugeInt temp;
	temp.intToHugeInt(d);
	temp=hug+temp;
	return temp;
}
hugeInt hugeInt::absMinus(hugeInt & h,hugeInt & hug)//����������ֵ����,��������ǰ�� this�ľ���ֵ����huge�ľ���ֵ
{
	hugeInt temp;
	int i;
	for(i=0;i<h.length;i++)
	{
		temp.intExpress[i]=h.intExpress[i]-hug.intExpress[i];
		
	}
	for(i=0;i<=h.length;i++)
	{
		if(temp.intExpress[i]<0)
		{
			temp.intExpress[i]+=10;
			temp.intExpress[i+1]-=1;
		}
	}
	temp.intArrayToCharArray();
	return temp;
}
hugeInt hugeInt::operator-( hugeInt & hug)//�������ļ���
{
	hugeInt temp;
	if(isPositive==true&&hug.isPositive==false)
	{
		return absPlus(*this,hug);
	}
	if(isPositive==false&&hug.isPositive==true)
	{
		return absPlus(*this,hug);
	}
	if(isPositive==true&&hug.isPositive==true)
	{
		if(abs_isLessThan(hug))
		{
			temp=absMinus(hug,*this);
			temp.isPositive=false;
		}
		else
			temp=absMinus(*this,hug);
		return temp;
	}
	else // false false
	{
		if(abs_isLessThan(hug)||abs_isEqualTo(hug))
		{
			temp=absMinus(hug,*this);
			temp.isPositive=true;
		}
		else 
		{
			temp=absMinus(*this,hug);
			temp.isPositive=false;
		}
		return temp;
	}
}
hugeInt hugeInt::operator*( hugeInt & hug )//�������ĳ˷�
{
	hugeInt temp;
	if(length+hug.length-1>PRECITION-1)
	{
		cout<<"�˷������\n";
		return temp;
	}
	//���Ŵ���
	if(isPositive==false&&hug.isPositive==true||isPositive==true&&hug.isPositive==false)
	{
		temp.isPositive=false;
	}
	if(isPositive==true&&hug.isPositive==true||isPositive==false&&hug.isPositive==false)
	{
		temp.isPositive=true;
	}
	int i,j,k;
	for(i=0;i<length;i++)
	{
		for(j=0;j<hug.length;j++)
		{
			temp.intExpress[i+j]+=intExpress[i]*hug.intExpress[j];
		}
	}
	for(k=0;k<length+hug.length;k++)
	{
		temp.intExpress[k+1]+=temp.intExpress[k]/10;
		temp.intExpress[k]%=10;
	}
	
	temp.intArrayToCharArray();
	return temp;
}
hugeInt operator*( hugeInt hug, int d )//1*a
{
	hugeInt temp;
	temp.intToHugeInt( d );
	return temp*hug;
}
hugeInt operator*( int d, hugeInt hug )
{
	return hug*d;
}
hugeInt hugeInt::operator/(  hugeInt & hug )//�������ĳ���
{

	/*hugeInt temp=*this;
	hugeInt temp2=hug;
	hugeInt r;
	temp.isPositive=true;
	temp2.isPositive=true;
	while(!temp.abs_isLessThan(temp2))
	{
		temp=temp-temp2;
		r=r+1;
	}
	if(isPositive==false&&hug.isPositive==true||isPositive==true&&hug.isPositive==false)
	{
		r.isPositive=false;
	}
	if(isPositive==true&&hug.isPositive==true||isPositive==false&&hug.isPositive==false)
	{
		r.isPositive=true;
	}
	return r;*/ //Ч�ʱȽϵ�
	hugeInt temp=*this;
	hugeInt temp2=hug;
	hugeInt r;
	temp.isPositive=true;
	temp2.isPositive=true;
	int len=temp.length;
	int itslen=temp2.length;
	int dert=len-itslen+1;
	for(int i=dert;i>=1;i--)
	{
		char * a=new char[dert+1];
		for(int j=0;j<i;j++)a[j]='0';
		a[0]='1';a[i]=0;
		hugeInt f(a);
		hugeInt ob=f*temp2;
		while( !temp.abs_isLessThan(ob) )
		{
		    temp=temp-ob;
		    r=r+f;
		}
	}
	if(isPositive==false&&hug.isPositive==true||isPositive==true&&hug.isPositive==false)
	{
		r.isPositive=false;
	}
	if(isPositive==true&&hug.isPositive==true||isPositive==false&&hug.isPositive==false)
	{
		r.isPositive=true;
	}
	return r;
}
hugeInt hugeInt::operator%( hugeInt & hug )//��������ģ
{
	hugeInt temp=*this;
	hugeInt temp2=hug;
	hugeInt r;
	temp.isPositive=true;
	temp2.isPositive=true;
	int len=temp.length;
	int itslen=temp2.length;
	int dert=len-itslen+1;
	for(int i=dert;i>=1;i--)
	{
		char * a=new char[dert+1];
		for(int j=0;j<i;j++)a[j]='0';
		a[0]='1';a[i]=0;
		hugeInt f(a);
		hugeInt ob=f*temp2;
		while( !temp.abs_isLessThan(ob) )
		{
		    temp=temp-ob;
		    r=r+f;
		}
	}
	if(isPositive==false&&hug.isPositive==true||isPositive==true&&hug.isPositive==false)
	{
		temp.isPositive=false;
	}
	if(isPositive==true&&hug.isPositive==true||isPositive==false&&hug.isPositive==false)
	{
		temp.isPositive=true;
	}
	return temp;
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////
//���дһ�����ڳ�������������࣬ʹ�����г�������ȷ���С�����ÿ���������������100λʮ����������


hugeInt GCD(hugeInt m, hugeInt n)  
{   
	hugeInt hi("0");
	if (m == hi)
	{
		return n;
	}
	if (n == hi)
	{
		return m;
	}
	hugeInt r1 = m, r2 = n, r3;   
	for( ; ; )   
	{   
		hugeInt q = r1 / r2;   
		q = q*r2;
		r3 = r1 - q ;   
		if( r3 == 0)   
			break;   

		r1 = r2;   
		r2 = r3;   
	}
	return r2;
}
int _tmain(int argc, _TCHAR* argv[])
{

	CStdioFile cstdfRead;
	CStdioFile cstdfWrite;
	wchar_t databuffer[16*1024];
	INT64 iNumOfCases;
	wchar_t * seps = L" \10\n";
	wchar_t * pwcToken;

	char numBuffer[128];
	INT64 iNumOfEvents;
	//vector<hugeInt> vecEvents;
	INT64 iTemp;

	cstdfRead.Open(L"D:\\B-small-attempt3.in.txt",CStdioFile::modeRead);
	//cstdfRead.Open(L"D:\\test.txt",CStdioFile::modeRead);
	cstdfWrite.Open(L"D:\\Projects\\2010\\CodeJam2010\\3\\3\\codejam.out.txt",CStdioFile::modeCreate);
	cstdfWrite.Close();
	cstdfWrite.Open(L"D:\\Projects\\2010\\CodeJam2010\\3\\3\\codejam.out.txt",CStdioFile::modeWrite);

	memset(databuffer,0,sizeof(databuffer));
	cstdfRead.ReadString(databuffer,sizeof(databuffer)-1);
	iNumOfCases = _wtoi(databuffer);

	for (int iIndex1 = 0;iIndex1 < iNumOfCases;iIndex1++)
	{
		printf("%d\n",iIndex1+1);
		memset(databuffer,0,sizeof(databuffer));
		cstdfRead.ReadString(databuffer,sizeof(databuffer)-1);
		pwcToken = wcstok(databuffer,seps);
		iNumOfEvents = _wtoi64(pwcToken);
		hugeInt * hiEvents = new hugeInt[iNumOfEvents];
		iTemp = 0;
		pwcToken = wcstok(NULL,seps);
		while(pwcToken!=NULL)
		{
			memset(numBuffer,0,sizeof(numBuffer));
			WideCharToMultiByte(CP_ACP,WC_COMPOSITECHECK,pwcToken,128,numBuffer,128,NULL,NULL);
			hugeInt hi(numBuffer);
			hiEvents[iTemp++] = hi;
			pwcToken = wcstok(NULL,seps);
		}
		QuickSortMore(hiEvents,iNumOfEvents);
		hugeInt hi1("0");
		hugeInt hi2;
		for(INT64 iIndex2 = 1;iIndex2<iNumOfEvents;iIndex2++)
		{
			hi2 = hiEvents[iIndex2-1] - hiEvents[iIndex2];
			hi1 = GCD(hi1,hi2);
			hi1.isPositive = true;
		}
		hugeInt hi3("0");
		hugeInt hi4 = hi3 - hiEvents[iNumOfEvents-1];
		while(true)
		{
			INT64 iIndex3;
			hi4 = hi4 + hi1;
			if (!hi4.isPositive)
			{
				continue;
			}
			for ( iIndex3 = 0;iIndex3<iNumOfEvents;iIndex3++)
			{
				if((hiEvents[iIndex3] + hi4)%hi1 != hi3)
					break;
			}
			if (iIndex3 == iNumOfEvents)
			{
				break;
			}
		}
		delete hiEvents;
		CString cstrout(hi4.primitive);
		memset(databuffer,0,sizeof(databuffer));
		wsprintf(databuffer,L"Case #%d: %s\n",iIndex1+1,cstrout);
		cstdfWrite.WriteString(databuffer);
	}

	cstdfRead.Close();
	cstdfWrite.Close();
	return 0;
}

