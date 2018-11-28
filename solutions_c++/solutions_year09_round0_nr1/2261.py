#include<vector>
#include<map>
#include<set>
#include<string>
#include<algorithm>
#include<cmath>
#include<fstream>
#include<iostream>
using namespace std;

int main()
{
   ifstream  in("A-large.in.txt",ios::in);
   ofstream  out("output.txt");
   int L,D,N,i=0,j,k;
   in>>L>>D>>N;string tp;
   vector<string> words;
   vector<string> samples;
   while(i++<D) 
   {in>>tp;words.push_back(tp);}
   i=0;
   while(i++<N)
   {in>>tp;samples.push_back(tp);}
   for(i=0;i<N;i++)
   {
       vector< set<char> > msg;
	   set<char> s;
	   for(j=0;j<samples[i].size();j++)
	   {
		   s.clear();
		   if(samples[i][j]=='(')
		   {
               j++;
			   while(samples[i][j]!=')')
			   {
                   s.insert(samples[i][j]);
				   j++;
			   }
			   msg.push_back(s);
			   continue;
		   }
		   else 
		   {
			   s.insert(samples[i][j]);
			   msg.push_back(s);
		   }
	   }
	   int num=0;
	   if(msg.size()!=L) {out<<"Case #"<<i+1<<": "<<num<<endl;continue;}
	   for(j=0;j<D;j++)
	   {
		   for(k=0;k<L;k++)
			   if(msg[k].find(words[j][k])==msg[k].end()) break;
		   if(k==L) num++;
       }
       out<<"Case #"<<i+1<<": "<<num<<endl;
   }
}