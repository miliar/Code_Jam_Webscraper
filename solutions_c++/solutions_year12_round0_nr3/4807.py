//#pragma   warning(disable:4503   4511   4512   4514   4663   4786) 
#pragma   warning(disable:4786) 
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	FILE *fpIn = fopen("C-small-attempt0.in","r");
	FILE *fpOut = fopen("2.txt","w");
	int num,a=0,b=0;
	vector<int> v;
	vector<int>::iterator vbegin,vend;
	fscanf(fpIn,"%d",&num);
	//cout<<num<<endl;
	for(int i=0; i<num; i++)//各行求
	{
		fscanf(fpIn,"%d %d",&a,&b);
		v.clear();
		ostringstream os;
		string s;
		string::iterator sbegin,send;
		os<<a;
		s = os.str();
		int ndigit = s.size();
		int n;//某一个数有几个循环在[a,b]中
		int result = 0;
		vbegin = v.begin();
		vend = v.end();
		for(int j=a; j<=b; j++)
		{
			/*os.str("");
			os<<j;
			s = os.str();//将j转换成字符串
			*/
			char buf[20];
			itoa(j,buf,10);
			s=buf;
			n=0;
			if(find(vbegin,vend,j)!=vend)
				continue;
			for(int k=1; k<ndigit; k++)//对J来说总共ndigit-1个循环
			{
				int sother;
				sbegin = s.begin();
				send = s.end();
				rotate(sbegin,send-1,send);
				istringstream is(s);
				is>>sother;
				v.push_back(j);
				vbegin = v.begin();
				vend = v.end();
				if(sother>=a && sother<=b && find(vbegin,vend,sother)==vend)//sother不在vector中
				{
					//fprintf(fpOut,"%d %d\n",j,sother);					
					v.push_back(sother);
					vbegin = v.begin();
					vend = v.end();
					n++;
				}
			}
		 	result += (n*(n+1)/2);	

		}
		//fprintf(fpOut,"[%d,%d]中有%d\n",a,b,result);
		//cout<<result;
		fprintf(fpOut,"Case #%d: %d\n",i+1,result);		
	}
	fclose(fpIn);
	fclose(fpOut);

/*	string s("12");
	string::iterator sbegin = s.begin();
	string::iterator send = s.end();
	rotate(sbegin,sbegin+1,send);
	cout<<s<<endl;
*/	
	return 0;
}