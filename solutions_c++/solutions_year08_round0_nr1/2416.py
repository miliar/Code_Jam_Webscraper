#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cstdio>

using namespace std;

int main()

{
    int t,s,q,cur,max_v,ans=-1,c=1,j;
    char tmp[120];
    vector<string> se,qr;
    bool flag;
    cin>>t;
    while(c <= t)
    {
        cin>>s;
        se.resize(s,"");
        for(int i = 0 ; i < s ; i++)
        {
            scanf(" %[^\n]",tmp);
            string e(tmp);
            //cout<<e<<endl;
            se[i] = e;
        }
        cin >> q;
        qr.resize(q,"");
        for(int i = 0 ; i < q ; i++)
        {
            scanf(" %[^\n]",tmp);
            string e(tmp);
            //cout<<e<<endl;
            qr[i] = e;
        }
        ans = 0;
        cur = 0;
        while(cur < q)
        {
            max_v = cur-1;
            
            
            for(int i = 0 ; i < s ; i++)
            {
                flag = false;
                for(j = cur ; j < q && qr[j] != se[i] ; j++);
                if(j == q) 
                {
                    cur = j;
                    flag = true;
                    break;
                }
                else if(j > max_v)
                {
                    max_v = j;
                }
            }
            if(!flag)
                {
                    cur = max_v;                    
                    ans++;
                }
        }
        cout << "Case #"<<c<<": "<<ans<<endl;
        c++;       
        
    }   
    return 0;                  
}
