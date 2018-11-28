#include<iostream>
#include<fstream>
#include<cstdio>

using namespace std;

#define REP(i,a,b) for(int i=a;i<b;++i)
#define RESET(v,t,s) memset(v,0,s*sizeof(t))

int main()
{
	ifstream fin("B-large.in");
	FILE* fp=fopen("B.o","w+");
	
	char temp1,temp2,temp3;
	
	int T,C,D,N;
	int start;
	
	char input[150];
	char combine[26][8][2];
	int opposite[26][8];
	int c_num[26];
	int d_num[26];
	int n_num[26];
	
cout<<"yaya"<<endl;
	
	fin>>T;
cout<<T<<endl;
	
	REP(t,0,T)
	{
		RESET(c_num,int,26);
		RESET(d_num,int,26);
		RESET(n_num,int,26);
		start=0;
		
cout<<"running case "<<t+1<<endl;
	
		fin>>C;
		REP(c,0,C)
		{
			fin>>temp1>>temp2>>temp3;
			combine[temp1-'A'][c_num[temp1-'A']][0]=temp2;
			combine[temp1-'A'][c_num[temp1-'A']][1]=temp3;
			++c_num[temp1-'A'];
			
			if(temp1!=temp2)
			{
				combine[temp2-'A'][c_num[temp2-'A']][0]=temp1;
				combine[temp2-'A'][c_num[temp2-'A']][1]=temp3;
				++c_num[temp2-'A'];
			}
		}
		fin>>D;
		REP(d,0,D)
		{
			fin>>temp1>>temp2;
			opposite[temp1-'A'][d_num[temp1-'A']]=temp2-'A';
			++d_num[temp1-'A'];
			if(temp1!=temp2)
			{
				opposite[temp2-'A'][d_num[temp2-'A']]=temp1-'A';
				++d_num[temp2-'A'];
			}
		}
		
		fin>>N;
		REP(n,0,N)
		{
			fin>>input[n];
			++n_num[input[n]-'A'];
			if(n>start)
			{
				//the combination
cout<<"c:"<<c_num[input[n]-'A']<<endl;
				REP(i,0,c_num[input[n]-'A'])
				{
					if(input[n-1]==combine[input[n]-'A'][i][0])
					{
						--n_num[input[n-1]-'A'];
						--n_num[input[n]-'A'];
						
printf("got a combine at %d: %c %c -> %c\n",n+1,input[n-1],input[n],combine[input[n]-'A'][i][1]);	
						
						input[n-1]=1;
						input[n]=combine[input[n]-'A'][i][1];
						break;
					}
				}
				
cout<<"d:"<<d_num[input[n]-'A']<<endl;
				
				REP(i,0,d_num[input[n]-'A'])
				{
					
cout<<(char)(opposite[input[n]-'A'][i]+'A')<<" "<<n_num[opposite[input[n]-'A'][i]]<<endl;

					if(n_num[opposite[input[n]-'A'][i]]>0)
					{
						start=n+1;
						RESET(n_num,int,26);
						
printf("got an opposite at %d: %c %c\n",n+1,opposite[input[n]-'A'][i]+'A',input[n]);
						
						break;						
					}
				}
			}	
		}
		fprintf(fp,"Case #%d: [",t+1);
REP(i,start,N)
	cout<<input[i];
cout<<endl;
		
		for(int i=start;input[i]==1;++i)
			++start;
		
		REP(i,start,N)
		{
			
cout<<start;
			if(input[i]>1)
			{
				if(i>start)
				{
					
cout<<" "<<i<<endl;
					fprintf(fp,", ");
				}
				fprintf(fp,"%c",input[i]);
			}
		}
		fprintf(fp,"]\n");
	}
	fclose(fp);
	return 0;
}
