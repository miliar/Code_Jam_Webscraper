#include<iostream>
#include<vector>
#include<queue>

using namespace std;

int main()
{
    long long cases, cont = 1;
    cin>>cases;
    while(cases--)
    {
        long long n, l, h;
        cin>>n>>l>>h;
        //priority_queue<long long, vector<long long>, less<long long> > q;
        vector<long> vec;
        
        for(long long i=0;i<n;++i)
        {
            long long k;
            cin>>k;
            vec.push_back(k);
        }
        /*
        bool flag = true;
        for(long long i=0;i<n && flag;++i)
            for(long long j=i;j<n;++j)
            {
                if(vec[i] < vec[j])
                {
                    if(vec[j] % vec[i] != 0)
                        flag = false;
                }
                else
                    if(vec[i] % vec[j] != 0)
                        flag = false;
                if(!flag)
                {
                    cout<<"Case #"<<cont<<": NO";
                    break;
                }
            }
        */
        int desde = min(l,h), hasta = max (l,h);
        bool flag = true;
        long long resp;
        for(long long i = desde; i<= hasta;++i)
        {
            flag = true;
            for(long long j=0;j<n && flag;++j)
            {
                if(i < vec[j])
                {
                    if(vec[j] % i != 0)
                    {
                        //cout<<vec[j]<<" "<<i<<endl;
                        flag = false;
                    }
                }
                else
                    if(i % vec[j] != 0)
                    {
                        //cout<<i<<" "<<vec[j]<<endl;
                        flag = false;
                    }
            }
            if(flag)
            {
                resp = i;
                cout<<"Case #"<<cont<<": "<<resp<<endl;
                break;
            }
        }
        if(!flag)
            cout<<"Case #"<<cont<<": NO"<<endl;
        ++cont;
    }
    return 0;
}
