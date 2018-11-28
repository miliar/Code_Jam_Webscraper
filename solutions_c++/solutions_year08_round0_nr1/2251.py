#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <conio.h>
#include <sstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define B begin()
#define E end()
#define II int i=0
#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define pi acos(-1.)
#define eps 1e-7
#define inf 1000000000
#define maxn 1100
#define maxp 1100000



//char -> int
int findlen(char* line)
{
	int i=0,num=0;
	while(line[i]!=NULL)
	{
		//cout<<line[i]-48;
		num=num + (line[i]-48);
		num=num*10;
		i++;
		//cout<<line[i];
	}

	//cout<<num/10;
	return num/10;
}

//round to 0.001 accuracy
double round(double n)
{
	int y;
	double z;
	z=n*1000;
	y=z;
	z=(double)y/1000;
	return z;
} 

//ceiling & floor
double cnf(double n)
{
	double cc = (ceil(n) - n);
	double ff = (n -floor(n));

	if( (ceil(n) - n) < 0.01)
		return ceil(n);
	else if( (n -floor(n)) < 0.01)
		return floor(n);
	else 
		return round(n);
}

//compare a,b 0.01 accuracy
bool cmpr(double a , double b)
{
	if(abs(a-b) < 0.01)
		return true;
	else 
		return false;
}


bool flag = 0; 

class par
{
	vector<char> vchar1,vchar2,vchar3,vchar4,vchar5,vchar6,final;
	vector<string> lstr1,lstr2;
	vector<int>vint1;
	vector<char>::iterator vic;
	vector<int>::iterator vii;
	string str1;
	//char *a,*b,*c;
	int space,start,end,len;
	int res1,res2;
	int no;
	int hit;
	bool pak;
	bool ac;
	bool ob;
	bool rt;
	bool isc;
	bool sca;
	float x1,y1,x2,y2,x3,y3;
	int eng,q;
public:
	void pareng(char *,int);
	void parq(char *,int);
	void display();
	char arr[200];
	char a[80];
	char b[20];
	char c[20];
	void cal();

//	float round(float);

};





void par::pareng(char *line,int n)
{
	if(flag == 0)
	{	eng = 0;
		q = 0;
		flag =1;
	}


	eng++;

	int i=0;
	space=0;
	len=0;
	start=0;
	no = n;

	str1=line;


	

	while(line[i]!=NULL)//find spaces
	{
		int j=0,k=0;
//--------------------------------------



		vchar1.push_back(line[i]);




	i++;
	}

			memset(a,0,80);
			int j = 0;
			
			for(int j=0;j<(int)vchar1.size();j++)
			{
				a[j]=vchar1[j];
			}
			
			str1=a;
			lstr1.push_back(str1);
			vint1.push_back(0);
			vchar1.clear();



}//pareng(char*)

void par::parq(char *line,int n)
{
	q++;

	int i=0;
	space=0;
	len=0;
	start=0;
	no = n;
	

	str1=line;


	while(line[i]!=NULL)//find spaces
	{
		int j=0,k=0;
//--------------------------------------



		vchar1.push_back(line[i]);




	i++;
	}

			memset(a,0,80);
			int j = 0;
			
			for(int j=0;j<(int)vchar1.size();j++)
			{
				a[j]=vchar1[j];
			}
			
			str1=a;
			lstr2.push_back(str1);

			vchar1.clear();


}//parq(int)


void par::display()
{
if(pak == true)
hit = 0 ;

sprintf(arr,"Case #%d: %d\n",no+1,space);



	eng = 0;
	q = 0;
	vint1.clear();
	vchar1.clear();
	lstr1.clear();
	lstr2.clear();
}//display


void par::cal()
{

int flag_itr = 0;
hit = 1;

	for(int i = 0 ; i<eng ; i++)
	{
	pak = true;
		for(int j = 0 ; j<q ; j++)
		{
			if(strcmp(lstr1[i].c_str(),lstr2[j].c_str()) == 0)
			{
				pak = false;
				
			}
			
		}
		if(pak == true)
			break;
	}


	for(int i = 0 ; i<q ; i++)
	{
	
		for(int j = 0 ; j<eng ; j++)
		{

			if(strcmp(lstr1[j].c_str(),lstr2[i].c_str()) == 0)
			{
			
				vint1[j]+=1;
			}
		}
			for(int i=0 ; i<eng ; i++)
			{
				flag_itr = 0;
				if(vint1[i] == 0)
				{
				flag_itr = 1;
				break;
				}
			}
			if(flag_itr == 0)
			{
				space++;
			//	flag_itr = 0;
				vint1.clear();
				i--;
				for(int i=0 ; i<eng ; i++)
				{
					vint1.push_back(0);
				}

			}

	}




/*
sprintf(arr,"Case #%d: %s %s %s",++no,a,b,c);
printf("%s\n\n",arr);
*/

}

	
int main(int argc, char* argv[])
{
int len,len2,len3;
char in_line[180];
char out_line[180];
int x1,y1,x2,y2,x3,y3;

ifstream fin("A.in",ios::binary);
ofstream fout("A.out",ios::binary);
if(!fin||!fout)
{

	cout<<"File io error";
	return 0;
}


fin.getline(in_line,80);
len=findlen(in_line);

par p;
//cout<<"Length is:"<<len<<'\n';
/*FILE *f;
f = fopen("a.in","rb");
fscanf(f,"%d",&len);
*/
for(int i =0 ; i<len ; i++)
{
	

	fin.getline(in_line,80);
	len2=findlen(in_line);

	for(int j =0 ; j<len2 ; j++)
	{
		fin.getline(in_line,80);
		p.pareng(in_line,i);
	}

	fin.getline(in_line,80);
	len3=findlen(in_line);

	for(int j =0 ; j<len3 ; j++)
	{
		fin.getline(in_line,80);
		p.parq(in_line,i);
	}

	p.cal();

	p.display();
	fout<<p.arr;
}







fin.close();
}