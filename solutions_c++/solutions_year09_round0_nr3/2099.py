#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<cstdio>
#include<Fstream>
using namespace std;
long double search_for(int i, map< int , vector<int> > m,int base);
string str="welcome to code jam";
int main()
{
 	 int t;
 	 FILE * fin1=fopen("C-small-attempt0.in","r");
      ofstream fout1("C-small-attempt0.out");
 	  fscanf(fin1,"%d\n",&t);
     
 	 for(int i1=0;i1<t;i1++)
 	 {
	  		 
	  		 char st[500];
	  		 char st2[100];
	  		 fgets(st,500,fin1);
	  		 string s(st);
	
             map< int , vector<int> > m;
	  		 
	  		 for(int i=0;i<s.size();i++)
	  		 {
	  		   for(int j=0;j<str.size();j++)
	  		   if(s[i]==str[j]){m[(int)s[i]].push_back(i);break;}
             }
             long double count=0; 
             count=search_for(0,m,-1);
             char ans[30];
             itoa(count,ans,10);
             string ans1(ans);
             if(ans1.size()>4)
             {
			   ans1=ans1.substr(ans1.size()-4); 				 
             }  
             else
             {
             while(ans1.size()!=4)
             ans1="0"+ans1;
			 }
             fout1<<"Case #"<<i1+1<<": "<<ans1<<endl;         
    }
    return 0;
}
long double search_for(int i, map< int , vector<int> > m,int base)
{
     //cout<<"str[i] "<<str[i]<<" base : "<<base<<endl;
     //getchar();
     if(i==str.size()){return 1;}
 	 if(m[(int)str[i]].size()==0){return 0;}
 	 vector<int> v=m[(int)str[i]];
 	 if(v[v.size()-1]< base){return 0;}
 	 
 	 
 	 long double count=0;
     for(int j=0;j<v.size();j++)
     {
       if(v[j]>base)
 	   count=count+search_for(i+1,m,v[j]);
     }
     {return count;}
}
 	 
 	 
