# include <iostream>
# include <Vector>
using namespace std;
string add(string a,int b)
{
       int c=(a[0]-'0')*10+(a[1]-'0');
       int d=(a[3]-'0')*10+(a[4]-'0');
       int e=d+b;
       if(e>=60) 
       {
                 d=e%60;c=c+e/60;
                 if(c>=24) c=c-24;
       }
       else d=e;
       string ans="00:00";
       if(c<10) ans[1]=('0'+c);
       else {ans[0]='0'+(c/10);ans[1]='0'+(c%10);}
       if(d<10) ans[4]=('0'+d);
       else {ans[3]='0'+(d/10);ans[4]='0'+(d%10);}
       /*if(c<10) ans="0"+('0'+c);
       else ans=""+('0'+(c/10))+('0'+(c%10));
       ans+=":";
       if(d<10) ans+=("0"+('0'+d));
       else ans+=(""+('0'+(d/10))+('0'+(d%10)));*/
       return ans;         
}
bool arr(vector<string> tr1,vector<string> tr2,int a)
{
        for(int i=0;i<tr1.size();i++)
                if(i!=a)
                        if(tr1[i]<=tr2[a] && tr2[i]>=tr2[a])
                                          return true;
        return false;
}
int main()
{
    int N;
    cin>>N;
    for(int z=0;z<N;z++)
    {
            int T,NA,NB;
            vector<string> tr1,tr2;
            vector<int> st;
            cin>>T>>NA>>NB;
            string a,b;
            for(int i=0;i<NA;i++)
                    {cin>>a>>b;tr1.push_back(a);tr2.push_back(b);st.push_back(1);}
            for(int i=0;i<NB;i++)
                    {cin>>a>>b;tr1.push_back(a);tr2.push_back(b);st.push_back(2);}
            for(int i=0;i<NA+NB;i++)
            {
                    string min=tr1[i];int p=i;
                    for(int j=i+1;j<NA+NB;j++)
                    {
                            if(tr1[j]<min) {min=tr1[j];p=j;}
                    }
                    string t=tr1[i];tr1[i]=tr1[p];tr1[p]=t;
                    t=tr2[i];tr2[i]=tr2[p];tr2[p]=t;
                    int t2=st[i];st[i]=st[p];st[p]=t2;
            }
            int ca=0,cb=0;
            while(true)
            {
                    int p=-1;
                    for(int i=0;i<NA+NB;i++)
                            if(st[i]==1 || st[i]==2)
                                        {p=i;break;}
                    if(p==-1) break;
                    if(st[p]==1) ca++; else cb++;
                    while(true)
                    {
                               //cout<<tr1[p]<<" "<<tr2[p]<<" "<<st[p]<<" "<<ca<<" "<<cb<<endl;
                               int te=st[p];
                               st[p]=3;
                               int p2=-1;
                               for(int i=p+1;i<NA+NB;i++)
                               {
                                       if(st[i]!=3 && st[i]!=te && tr1[i]>=add(tr2[p],T))
                                                   {p2=i;break;}
                               }
                               if(p2==-1) break;
                               //cout<<"("<<tr1[p]<<" "<<tr2[p]<<" "<<st[p]<<" "<<tr1[p2]<<" "<<tr2[p2]<<" "<<st[p2]<<")\n";
                               p=p2;
                    }
            }
            cout<<"Case #"<<z+1<<": "<<ca<<" "<<cb<<endl;
    }
    return 0;
}
