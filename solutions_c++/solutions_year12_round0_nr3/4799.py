#include<iostream>
#include<sstream>
#include<vector>
using namespace std;

int changeToNumber(string str)
{
    stringstream num(str);
    int x;
    num >> x;
    return x;
}
int numDigits(int number)
{
    int digits = 0;
    while (number) {
        number /= 10;
        digits++;
    }
    return digits;
}
string numToString(int Number)
{
    string String = static_cast<ostringstream*>( &(ostringstream() << Number) )->str();
    return String;
}
vector<int> process(string str,int num)
{
           vector<int> out;
           string temp=str.substr(0,num);
           int org=changeToNumber(temp);
           for(int i=1;i<(str.length()-num);i++)
           {
                   temp=str.substr(i,num);
                   int final=changeToNumber(temp);
                   if(numDigits(final)==num && final>org)
                   out.push_back(final);
           }  
           if(out.empty()) out.push_back(-1);
           return out;  
}
               
               
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("recycle1.txt","w",stdout);
    vector < vector<int> > v;
    for(int i=0;i<1001;i++)
    {
                          int numOfDigits = numDigits(i);
                          string str=numToString(i);
                          str+=str;
                          vector<int> temp=process(str,numOfDigits);
                          v.push_back(temp);
    }    

    int N,cases=0;
    cin>>N;
    while(N--)
    {
              int ans=0;
              cases++;
              int a,b;
              cin>>a>>b;
              for(int i=a;i<=b;i++)
              {
                         vector<int>::iterator it = v[i].begin();
                          for (; it < v[i].end(); it++) 
                          {
                              int k= *it;
                              if(k<=b && k>a)
                              ans++;
                          }
              }
              cout<<"Case #"<<cases<<": "<<ans<<"\n";

    }
}
              
              
