#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;
int turntime,a;
vector<int> depa, arra, depb, arrb;
void f1(string str)
{
     int t1=0;
     t1=(str[0]-'0')*10;  t1+=(str[1]-'0');
     t1*=60;
     t1+=(str[3]-'0')*10; t1+=(str[4]-'0');
     depa.push_back(t1);
     t1=0;
     t1=(str[6]-'0')*10; t1+=(str[7]-'0');
     t1*=60;
     t1+=(str[9]-'0')*10; t1+=str[10]-'0';
     t1+=turntime;
     arrb.push_back(t1);
}
void f2(string str)
{
     int t1;
     t1=0;
     t1=(str[0]-'0')*10;  t1+=(str[1]-'0');
     t1*=60;
     t1+=(str[3]-'0')*10; t1+=(str[4]-'0');
     depb.push_back(t1);
     t1=0;
     t1=(str[6]-'0')*10; t1+=(str[7]-'0');
     t1*=60;
     t1+=(str[9]-'0')*10; t1+=str[10]-'0';
     t1+=turntime;
     arra.push_back(t1);
}
bool isin(int n, vector<int> v)
{
     for(int i=0;i<v.size();i++)
       if(v[i]==n)
         return true;
     return false;
}
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("c-output4.txt");
    int t,i,ansa,ansb,numa,numb,na,nb,cas=1;
    fin>>t;
    char stri[100];   string str;
    while(t--)
    {
        ansa=0; ansb=0; numa=0; numb=0;
        arra.clear(); arrb.clear(); depa.clear(); depb.clear();
        fin>>turntime>>na>>nb;
        fin.getline(stri,100);
        for(i=0;i<na;i++)
        {
           fin.getline(stri,100);
           str=stri;
           f1(str);
        }
        for(i=0;i<nb;i++)
        {
           fin.getline(stri,100);
           str=stri;
           f2(str);
        }
        sort(arra.begin(), arra.end());
        sort(depa.begin(), depa.end());
        a=0;
        /*for(i=0;i<1440;i++)
        {
           if(isin(i,arra)==true)
             numa++;
           if(isin(i,arrb)==true)
             numb++;
           if(isin(i,depa)==true)
           {
              if(numa>0)
                numa--;
              else
                ansa++;
           }
           if(isin(i,depb)==true)
           {
               if(numb>0)
                 numb--;
               else 
                 ansb++;
           }
        }*/
        for(i=0;i<depa.size();i++)
        {
            if((a<arra.size())&&(arra[a]<=depa[i]))
            {  a++; }
            else
            {  ansa++; }
        }
        sort(depb.begin(), depb.end());
        sort(arrb.begin(), arrb.end());
        a=0;
        for(i=0;i<depb.size();i++)
        {
           if((a<arrb.size())&&(arrb[a]<=depb[i]))
           {  a++; }
           else
             ansb++;
        }
        fout<<"Case #"<<cas<<": "<<ansa<<" "<<ansb<<endl;
        cas++;
    }
    return 0;
}
