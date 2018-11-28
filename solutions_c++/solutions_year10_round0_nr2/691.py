// B.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <fstream>
using namespace std;

template<class T>
 T MAX( T a, T b)
{
	if(a<b)
		return b;
	else
		return a;
}

template<class T>
 T MIN( T a, T b)
{
	if(a<b)
		return a;
	else return b;
}
template<class T>
void swap(T *a,T *b)
{
	T t=*a;
	*a=*b;
	*b=t;
}

int gcd(int a,int b)
{
	if(a<b)
		swap(a,b);

	if(b==0)
		return a;
	else
		return gcd(b,a%b);
}


int toINT(char c)
{
	return c-'0';
}

string clearFrontZero(const string & str)
{
	string s(str);
	int pos,count=0;
	for(pos=0;pos<s.size();pos++)
		if(str[pos]=='0')
			count++;
		else
			break;
	s.erase(0,count);
	return s;
}

bool operator<(const string &str1,const string &str2)
{
	string A(str1),B(str2);
	A=clearFrontZero(A);
	B=clearFrontZero(B);
	if(A.size()<B.size())
		return true;
	else if(A.size()>B.size())
		return false;
	else
	{
		for(int i=0;i<A.size();i++)
			if(A[i]<B[i])
				return true;
			else {
				if(A[i]>B[i])
					return false;
			}
		return false;//A==B
	}
}

string strAdd(const string & str1,const string &str2)
{
	string A(str1),B(str2);
	A=clearFrontZero(A);
	B=clearFrontZero(B);
	unsigned int A_size=A.size(),B_size=B.size();
	int i,j,k;
	unsigned int max_size=MAX(A_size,B_size);
	unsigned int min_size=MIN(A_size,B_size);
	if(A<B)
		swap(A,B);
	reverse(A.begin(),A.end());
	reverse(B.begin(),B.end());
	int *carry=new int[max_size+1];
	for(i=0;i<max_size+1;i++)
	{
		carry[i]=0;
	}
	for(i=0;i<max_size;i++)
	{
		if(i<min_size)
		{
			if(toINT(A[i])+toINT(B[i])+carry[i]>9)
			{
				A[i]=toINT(A[i])+toINT(B[i])+carry[i]-10+'0';
				carry[i+1]=1;
			}
			else
			{
				A[i]=toINT(A[i])+toINT(B[i])+carry[i]+'0';
			}
		}
		else
		{
			if(toINT(A[i])+carry[i]>9)
			{
				A[i]=toINT(A[i])+carry[i]-10+'0';
				carry[i+1]=1;				
			}
			else
			{
				A[i]=toINT(A[i])+carry[i]+'0';
			}
		}
	}
	if(carry[i])
		A+='1';
	reverse(A.begin(),A.end());
	return A;
}

string strSub(const string& str1,const string& str2)
{
	string A(str1),B(str2);
	A=clearFrontZero(A);
	B=clearFrontZero(B);
	unsigned int A_size=A.size(),B_size=B.size();
	int i,j,k;
	unsigned int max_size=MAX(A_size,B_size);
	unsigned int min_size=MIN(A_size,B_size);
	if(A<B)
		swap(A,B);
	reverse(A.begin(),A.end());
	reverse(B.begin(),B.end());
	int *carry=new int[max_size+1];
	for(i=0;i<max_size+1;i++)
	{
		carry[i]=0;
	}

	for(i=0;i<max_size;i++)
	{
		if(i<min_size)
		{
			if(A[i]-B[i]-carry[i]>=0)
				A[i]=A[i]-B[i]-carry[i]+'0';
			else
			{
				A[i]=A[i]-B[i]-carry[i]+'0'+10;
				carry[i+1]=1;
			}
		}
		else
		{
			if(A[i]-'0'-carry[i]>=0)
				A[i]=A[i]-carry[i];
			else
			{
				A[i]=A[i]-carry[i]+10;
				carry[i+1]=1;
			}
		}

	}
	reverse(A.begin(),A.end());
	A=clearFrontZero(A);
	delete [] carry;
	if(A.empty())
		A="0";
	return A;

}

string strMul(const string &str1,const string &str2)
{
	string s1(str1),s2(str2);
	reverse(s1.begin(),s1.end());
	reverse(s2.begin(),s2.end());
	string result;
	int i,j,k;

	const int M1=s1.size();
	const int M2=s2.size();
	//将字符串base转化为int
	int *b1 = new int[M1];
	for(i=0;i<M1;i++)
		b1[i]=s1[i]-'0';
	int *b2 = new int[M2];
	for(i=0;i<M2;i++)
		b2[i]=s2[i]-'0';
	//初始化相乘矩阵
	int **pMul = new int*[M1];
	for(i=0;i<M1;i++)
		pMul[i] = new int[M1+M2];

	for(i=0;i<M1;i++)
		for(j=0;j<M1+M2;j++)
			pMul[i][j]=0;
	//初始化结果向量
	int *pResult = new int[M1+M2];
	for(i=0;i<M1+M2;i++)
		pResult[i]=0;

	//乘法运算
	for(i=0;i<M1;i++)
		for(j=0;j<M2;j++)
		{
			pMul[i][i+j]+=b1[i]*b2[j];
			pMul[i][i+j+1]+=pMul[i][i+j]/10;
			pMul[i][i+j]%=10;
		}

		for(i=0;i<M1;i++)
		{
			for(j=0;j<M1+M2;j++)
			{
				//	cout<<pMul[i][j]<<" ";
			}
			//	cout<<endl;
		}
		//结果相加
		for(j=0;j<M1+M2;j++)
		{
			for(i=0;i<M1;i++)
			{
				pResult[j]+=pMul[i][j];
			}
			if(j+1!=M1+M2)
				pResult[j+1]+=pResult[j]/10;
			pResult[j]%=10;
		}

		for(i=0;i<M1+M2;i++)
			result+=pResult[i]+'0';
		reverse(result.begin(),result.end());

		result=clearFrontZero(result);

		return result;
}


string strDev(const string &str1,const string &str2)
{
	string s1(str1),s2(str2);
	reverse(s1.begin(),s1.end());
	reverse(s2.begin(),s2.end());
	string result;
	int i,j,k;

	const int M1=s1.size();
	const int M2=s2.size();
	//将字符串base转化为int
	int *b1 = new int[M1];
	for(i=0;i<M1;i++)
		b1[i]=s1[i]-'0';
	int *b2 = new int[M2];
	for(i=0;i<M2;i++)
		b2[i]=s2[i]-'0';
	//初始化相乘矩阵
	int **pMul = new int*[M1];
	for(i=0;i<M1;i++)
		pMul[i] = new int[M1+M2];

	for(i=0;i<M1;i++)
		for(j=0;j<M1+M2;j++)
			pMul[i][j]=0;
	//初始化结果向量
	int *pResult = new int[M1+M2];
	for(i=0;i<M1+M2;i++)
		pResult[i]=0;

	//乘法运算
	for(i=0;i<M1;i++)
		for(j=0;j<M2;j++)
		{
			pMul[i][i+j]+=b1[i]*b2[j];
			pMul[i][i+j+1]+=pMul[i][i+j]/10;
			pMul[i][i+j]%=10;
		}

		for(i=0;i<M1;i++)
		{
			for(j=0;j<M1+M2;j++)
			{
				//	cout<<pMul[i][j]<<" ";
			}
			//	cout<<endl;
		}
		//结果相加
		for(j=0;j<M1+M2;j++)
		{
			for(i=0;i<M1;i++)
			{
				pResult[j]+=pMul[i][j];
			}
			if(j+1!=M1+M2)
				pResult[j+1]+=pResult[j]/10;
			pResult[j]%=10;
		}

		for(i=0;i<M1+M2;i++)
			result+=pResult[i]+'0';
		reverse(result.begin(),result.end());

		result=clearFrontZero(result);

		return result;
}

string strRemainder(const string &str1,const string &str2)
{
	string A(str1),B(str2);
	A=clearFrontZero(A);
	B=clearFrontZero(B);
	unsigned int A_size=A.size(),B_size=B.size();
	int i,j,k;
	unsigned int max_size=MAX(A_size,B_size);
	unsigned int min_size=MIN(A_size,B_size);

	while(!(A<B))
	{
		while(A.size()>=B.size())
		{
			string tempB(A.size()-B.size(),'0');
			tempB=B+tempB;
			if(A<tempB)
				tempB=tempB.substr(0,tempB.size()-1);
			//			cout<<A<<"  "<<tempB<<" "<<MIN(A,tempB)<<endl;

			while(tempB<A || tempB==A)
			{
				A=strSub(A,tempB);
				if(A<B)
					return A;
			}
		}	
		if(A<B)
			return A;
	}
	return A;
}

string strMod(const string &str1,const string &str2)
{
	string A(str1),B(str2);
	A=clearFrontZero(A);
	B=clearFrontZero(B);
	unsigned int A_size=A.size(),B_size=B.size();
	int i,j,k;
	unsigned int max_size=MAX(A_size,B_size);
	unsigned int min_size=MIN(A_size,B_size);

	if(A<B)
		swap(A,B);
	if(A==B)
		return A;
	while(!(A.size()<10 && B.size()<10))
	{
		if(A==B)
			return A;
		if(A<B)
			swap(A,B);
		while(A.size()>=B.size())
		{
			string tempB(A.size()-B.size(),'0');
			tempB=B+tempB;
			if(A<tempB)
				tempB=tempB.substr(0,tempB.size()-1);
//			cout<<"FUCK"<<A<<"  B= "<<B<<" "<<tempB<<" "<<MIN(A,tempB)<<endl;
			
			while(!tempB.empty() && (tempB<A || tempB==A) )
				A=strSub(A,tempB);
			if(A=="0")
				return B;
			if(A==B)
				return A;
			if(A=="1")
				return A;
			if(A<B)
				swap(A,B);
		}
		if(A.size()==0)
			return B;
	}
	int intA=0,intB=0;
	for(i=0;i<A.size();i++)
		intA=intA*10+toINT(A[i]);
	for(i=0;i<B.size();i++)
		intB=intB*10+toINT(B[i]);
//	cout<<intA<<" "<<intB<<endl;
	int result=gcd(intA,intB);
	string strA;
	char c;
	while(result)
	{
		c=result%10+'0';
		result/=10;
		strA=c+strA;		
	}
	if(strA.empty())
		strA="0";
	return strA;	
}

int  partition(string *p,int l,int r)
{
	string str=p[l];
	int i,k=l;
	for(i=1+l;i<=r;i++)
	{
		if(p[i]<str)
			swap(&p[i],&p[++k]);
	}
	swap(&p[k],&p[l]);
	return k;
}

void quicksort(string *p,int l,int r)
{
	if(l<r)
	{
		int k=partition(p,l,r);
		quicksort(p,l,k-1);
		quicksort(p,k+1,r);
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	fstream in,out;
	in.open("B-large.in",ios::in);
	out.open("B-large.out",ios::out);

	int i,j,k;
	string str,result;
	vector<string> svec;
	vector<string>::iterator iter;
	string ps[1001];
	string distance[1001];

/*
	while(cin>>str>>result)
	cout<<strRemainder(str,result)<<endl;*/



	int C;
	int N;
	in>>C;
	
	for(i=0;i<C;i++)
	{
		in>>N;
		for(j=0;j<N;j++)
		{
			in>>ps[j];
		}

		quicksort(ps,0,N-1);

/*

		for(j=0;j<N;j++)
			cout<<ps[j]<<" ";
		cout<<endl;
*/



		for(j=0;j<N-1;j++)
			distance[j]=strSub(ps[j+1],ps[j]);
		quicksort(distance,0,N-2);





		for(j=0;j<N-1;j++)
			if(distance[j]!="0")
			{
				str=distance[j];
				break;
			}
//		cout<<str<<endl;
//			cout<<"j="<<j<<endl;
		for(j;j<N-1;j++)
		{
//			cout<<str<<" "<<distance[j];
			str=strMod(str,distance[j]);
			if(str=="1")
				break;
		}
//		cout<<"str= "<<str<<endl;
	
			if(str=="1")
					result="0";
				else
				{
					result=strRemainder(ps[0],str);
//					cout<<str<<endl;
					if(result!="0")
						result=strSub(str,result);
				}
				out<<"Case #"<<1+i<<": "<<result<<endl;
		
		
	}


	in.close();
	out.close();
	return 0;
}

