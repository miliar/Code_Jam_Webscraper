#include<iostream>
#include<fstream>

using namespace std;

ifstream fin("Blarge.in");
ofstream fout("Bout.txt");
int main()
{
    int T;
    fin >> T;
    for(int i=1;i<=T;i++)
    {
        int N,S,p,temp;
        fin >> N >> S >> p;
        int s = 0;
        int ans = 0;
        for(int n=0;n<N;n++)
        {
            fin >> temp;
            if(temp==0&&p==1)continue;
            if(temp>=3*p-2)ans++;
            else if (temp>=3*p-4)s++;
        }
        if(s<=S)ans+=s;
        else ans+=S;
        fout << "Case #" << i << ": "<< ans << endl;
    }
    
}
