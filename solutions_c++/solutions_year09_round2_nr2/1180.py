#include<iostream>
#include<fstream>
#include<cstring>
#include<list>
using namespace std;
int main()
{
    ifstream input("input.txt");
    ofstream output("output.txt");
    long long int i,j,k,l,m,n,T,C;
    bool isdone;
    char orgnum[40];
    input>>T;
    for(i=0;i<T;i++)
    {
    char strnum[40];
    input>>strnum;
    strcpy(orgnum,strnum);
    int minpos;
    char temp;
    isdone=false;
//    cout<<"CASE: "<<strnum<<"\n";
    if(strlen(strnum)>1)
    {
    for(j=strlen(strnum)-2;j>=0 && isdone==false;j--)
    {
                                minpos=-1;
  //                              cout<<"for j="<<strnum[j]<<"\n";
                                for(k=j+1;k<strlen(strnum);k++)
                                {
                                         //cout<<"it "<<strnum[j]<<" "<<strnum[k]<<"\n";
                                         if(strnum[j]<strnum[k])
                                         {
                                                                
                                                              //  cout<<"atlest here minpos="<<minpos<<"\n";
                                                                if(minpos==-1)
                                                                minpos=k;
                                                                else 
                                                                {
                                                                //cout<<"asdfsafs "<<strnum[minpos]<<" "<<strnum[k]<<"\n";     
                                                                if(strnum[minpos]>strnum[k])
                                                                minpos=k;                                                                
                                                                }
                                         }
                                }
                                 //        cout<<"minpos="<<minpos<<"\n";
                                         if(minpos!=-1)
                                         {
                                //                       cout<<"minpos no="<<strnum[minpos]<<"\n";
                                                       temp=strnum[j];
                                                       strnum[j]=strnum[minpos];
                                                       strnum[minpos]=temp;
                                  //                     cout<<"now number="<<strnum<<"\n";
                                                       list<int> remno;
                                                       for(k=j+1;k<strlen(strnum);k++) remno.push_back(strnum[k]);
                                                       remno.sort();
                                                       list<int>::iterator it=remno.begin();
                                                       for(k=j+1;it!=remno.end();it++,k++)
                                                       {
                                                                                      strnum[k]=*it;
                                                       }
                                                       isdone=true;
                                                       break;
                                         
                                         }
    }
    }
    if(isdone==false)
    {
                     list<int> numbers;
                     for(j=0;j<strlen(orgnum);j++)
                     numbers.push_back(orgnum[j]);
                     numbers.sort();
                     list<int>::iterator it=numbers.begin();
                     list<int>::iterator it1=numbers.begin();
                     while(*it1=='0') it1++;
                     strnum[0]=*it1;
                     strnum[1]='0';
                     j=2;
                     for(;it!=numbers.end();it++)
                     {
  //                   cout<<"writing "<<(*it-'0')<<"\n";
                     if(it!=it1)
                     strnum[j++]=*it;
                     }
                     strnum[strlen(orgnum)+1]='\0';
    }
    //cout<<"done "<<strnum<<"\n";
    output<<"Case #"<<(i+1)<<": "<<strnum<<"\n";
  //  cin>>j;
}          

    input.close();
    output.close();
   
    return 0;
}
