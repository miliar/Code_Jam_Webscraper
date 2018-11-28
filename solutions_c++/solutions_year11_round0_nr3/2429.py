#include<iostream>
#include<fstream>
using namespace std;
//ifstream fin("CANSPLIT.IN");
ifstream fin("C-large.in");
ofstream fout("C-large.out");
int A[1001];
string S[1001];
int P[1001];
int N;

string convert(int n)
{
    string ret = "";
    while(n != 0)
    {
        if(n%2==0)
            ret+="0";
        else
            ret+="1";
        n/=2;
    }
    int len = ret.length();
    for(int i=0;i<len/2;i++)
        swap(ret[i],ret[len-1-i]);
    return ret;
}

string addzeros(string s,int len)
{
    string ret = "";
    for(int i=0;i<len-(int)s.length();i++)
        ret+="0";
    ret+=s;
    return ret;
}

int Sean(int pos)
{
    fill(P,P+S[pos].length(),0);
    for(int i=1;i<=N;i++)
       if(i!=pos)
          for(int j=0;j<S[i].length();j++)
              P[j] += S[i][j]-'0';
    
    for(int i=0;i<S[pos].length();i++)
       if(S[pos][i]-'0'!=P[i]%2)
          return 0;
          
    int ret = 0;
    for(int i=1;i<=N;i++)
       if(i!=pos)
          ret += A[i];
    return ret;
}

void process(int t)
{
    fout<<"Case #"<<t<<": "; 
    int Max = 0; 
    fin>>N;
    for(int i=1;i<=N;i++)
    {
        fin>>A[i];
        Max = max(Max,A[i]);
    }
    string s = convert(Max);
    for(int i=1;i<=N;i++)
    {
        S[i] = convert(A[i]);
        S[i] = addzeros(S[i],s.length());
    }
    Max = 0;
    for(int i=1;i<=N;i++)
        Max = max(Max,Sean(i));
    if(Max==0)
       fout<<"NO\n";
    else
       fout<<Max<<endl;
}

int main()
{
    int T;
    fin>>T;
    for(int i=1;i<=T;i++)
        process(i);    
//    system("pause");
    return 0;
}
