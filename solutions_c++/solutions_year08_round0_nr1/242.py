#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string s[1000], q[1000];
int S, Q;

int GetLen(string word, int from)
{
    int i;
    for (i=from;i<Q && word!=q[i];i++);
    return i;
}
int GetMax(int from)
{
    int max=0, maxI=0, i, x;
    for (i=0;i<S;i++)
    {
        x=GetLen(s[i], from);
        if (x>max)
        {
            max = x;
            maxI= i;
        }
    }
    return maxI;
}

int main()
{
    int N, t, i;
    ifstream in("input.txt", ios::in);
    ofstream out("output.txt", ios::out);
    char str[256];
    
    in >> N;
    
    for (t=1;t<=N;t++)
    {
        in >> S;
        in.get();
        for (i=0;i<S;i++)
        {
            in.getline(str, 256);
            s[i]=str;
            //cout << s[i] << endl;
        }
        in >> Q;
        //cout << endl;
        in.get();
        for (i=0;i<Q;i++)
        {
            in.getline(str, 256);
            q[i]=str;
            //cout << q[i] << endl;
        }
        //cout << endl;
        
        int curr, res=0;
        curr = GetMax(0);
        for (i=0;i<Q;i++)
        {
            if (q[i]==s[curr])
            {
                res++;
                curr = GetMax(i);
            }
        }
        out << "Case #" << t << ": " << res << endl;
    }
    
    in.close();
    out.close();
    
    return 0;
}
