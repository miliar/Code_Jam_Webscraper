#include<iostream>
#include<vector>
#include<fstream>
//#include<conio.h>
using namespace std;
vector<string> engname,qname;
vector<int> near;
int s,q;
void setnull()
{
     for(int i=0; i<near.size() ; i++)
       near[i]=-1;
}
int getpos(string s)
{
    for(int i=0;i<engname.size();i++)
      if(engname[i]==s)
        return i;
}
void init(int st)
{
     int i,j;
    /* for(i=st;i<qname.size();i++)
     {
         if(near[getpos(qname[i])]==-1)
           near[i]=i;
     }*/
     for(i=0;i<engname.size();i++)
     {
          for(j=st; j<qname.size();j++)
            if((engname[i]==qname[j])&&(near[i]==-1))
            {  near[i]=j; break; }
     }
     for(i=0;i<near.size();i++)
       if(near[i]==-1)
         near[i]=100000;
}
int max()   //  pos of max
{
   int max=0,i;
   for(i=1;i<near.size();i++)
     if(near[i]>=near[max])
       max=i;
   return max;
}
int f(int st)
{
    setnull();
    init(st);
    
   /* cout<<"st= "<<st<<" "<<"near= ";
    for(int i=0;i<near.size();i++)
      cout<<near[i]<<" ";
    cout<<endl;*/
    
    int m=max();
    if(near[m]==100000)
      return 0;
    return 1+f(near[m]);   
}
int main()
{
    int t,i,ans,cas=1;
    ifstream fin("A-large.in");
    ofstream fout("hihihi.txt");
    char str[100];
    fin>>t;
    while(t--)
    {
              fin>>s;
              engname.resize(s);
              fin.getline(str,100);
              for(i=0;i<s;i++)
              {  fin.getline(str,100); engname[i].assign(str); }
              fin>>q;
              fin.getline(str,100);
              qname.resize(q);
              for(i=0;i<q;i++)
              {  fin.getline(str,100); qname[i].assign(str); }
              
              near.resize(s);    // not in s denoted by 100000
              //init(0);
              ans=f(0);
              fout<<"Case #"<<cas<<": "<<ans<<"\n";
              cas++;
              cout<<cas-1<<" ";
             /* for(i=0;i<engname.size();i++)
                cout<<engname[i]<<endl;
              cout<<endl;
              for(i=0;i<qname.size();i++)
                cout<<qname[i]<<endl;*/

    }
   // getch();
    return 0;
}
