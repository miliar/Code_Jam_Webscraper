#include <iostream> 
#include <vector>
#include <string>
#include <string.h>
#include <algorithm> 
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cfloat>
#include <bitset> 

using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

 map < pair<string,string> ,bool > mapa;
 long double tudo(string num)
 {
    long double re;
    stringstream is(num);
    is>>re;
    return re;
 }
 void par1(string &cad)
{
    string res3="";
    int i=0;
    while(i<cad.size())
    {
        
        if(cad[i]=='(')
        {   
            res3+=cad[i];
            i++;
            while(i<cad.size()&&cad[i]==' ')
            {
                i++;
            }
            //if(i<cad.size())
            //res3+=cad[i];
        }
        else
        {
        res3+=cad[i];
        i++;
        }
    }
    cad=res3;
}
void par2(string &cad)
{
    int i=cad.size()-1;
    string res3="";
    while(i>=0)
    {
        if(cad[i]==')')
        {
            res3=cad[i]+res3;
            i--;
            while(i>=0&&cad[i]==' ')
            {
                i--;
            }
            //i++;
            //if(i>=0)
            //res3=cad[i]+res3;
        }
        else
        {
        res3=cad[i]+res3;
        i--;
        }
    }
    cad=res3;
}
 void pasa(string eva,string &cad1,string &cad2,string &cad3,string &cad4)
 {
        int ini=0;
        cad1="";
        while(eva[ini]==' ')
        ini++;
        while(eva[ini]!=' ')
        {
            cad1+=eva[ini];
            ini++;
        }
        while(eva[ini]==' ')
        ini++;
        cad2="";
        while(eva[ini]!=' ')
        {
            cad2+=eva[ini];
            ini++;
        }
          while(eva[ini]==' ')
        ini++;
        int iz=1;
        ini++;
        cad3="(";
       
        while(iz!=0&&ini<eva.size())
        {
            if(eva[ini]=='(')
            iz++;
            else if(eva[ini]==')')
            iz--;
            cad3+=eva[ini];
            ini++;
        }
         while(eva[ini]==' ')
        ini++;
        cad4="(";
        ini++;
        iz=1;
        while(iz!=0&&ini<eva.size())
        {
            if(eva[ini]=='(')
            iz++;
            else if(eva[ini]==')')
            iz--;
            cad4+=eva[ini];
            ini++;
        }
        
 
 }
long double funcion(string animal,long double tengo,string todo2)
{
    string eva=todo2.substr(1,todo2.size()-2);
    string a,b,c,d;
    stringstream is(eva);
    is>>a>>b>>c>>d;
    //cout<<a<<" "<<b<<" "<<c<<" "<<d<<endl;
   //cout<<eva<<endl;
   string cad1,cad2,cad3,cad4;
    long double prob=tudo(a);
    if(b.size()==0)
    {
    return tengo*prob;
    }
    else
    {
        pasa(eva,cad1,cad2,cad3,cad4);
      // cout<<cad1<<" "<<cad2<<" "<<cad3<<" "<<cad4<<endl;
        
      //cout<<cad1<<" "<<cad2<<" "<<cad3<<" "<<cad4<<endl;
        prob=tudo(cad1);
        if(mapa[make_pair(animal,cad2)]==true)
        {
         par1(cad3);
        par2(cad3);
        return funcion(animal,tengo*prob,cad3);
        }
        else
        {
        par1(cad4);
        par2(cad4); 
        return funcion(animal,tengo*prob,cad4);
        }
    }
return 1.0;
}

int main()
{
int n,m;

cin>>n;

string cad;
getline(cin,cad);

for(int ii=0;ii<n;ii++)
{
    cin>>m;
    string res;
    res="";
    //cout<<res<<endl;
    getline(cin,cad);
    for(int j=0;j<m;j++)
    {
        getline(cin,cad);
        res+=cad;
    }
    par1(res);
    //cout<<res<<endl;
    par2(res);
    cin>>m;
    int num;
    string animal,habilidad;
   mapa.clear();
   vector <string> todos(m);
    for(int i=0;i<m;i++)
    {   
        cin>>animal>>num;
        todos[i]=animal;
        for(int j=0;j<num;j++)
        {
            cin>>habilidad;
            mapa[make_pair(animal,habilidad)]=true;
        }
    }
    long double res2;
    printf("Case #%d:\n",ii+1);
    for(int i=0;i<todos.size();i++)
    {
        res2=funcion(todos[i],1.0,res);
        printf("%.7Lf\n",res2);
    }
    
    
}

/*
string cad1,cad2,cad3,cad4;
pasa("00.5 cool  (11.000)  (00.5)",cad1,cad2,cad3,cad4);
cout<<cad1<<" "<<cad2<<" "<<cad3<<" "<<cad4<<endl;*/
return 0;
}
