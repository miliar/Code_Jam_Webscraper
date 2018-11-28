# include <iostream>
# include <vector>
# include <string>

using namespace std;

void transform (vector <char>& ans,string trans)
{
     int size = ans.size ();
     if (ans[size - 1] == trans[0] && ans[size - 2] == trans[1] ||
         ans[size - 1] == trans[1] && ans[size - 2] == trans[0])
         {
                  ans.pop_back();
                  ans.pop_back();
                  ans.push_back (trans[2]);
         }
}    

void checkoppose (vector <char>& ans,string oppose)
{
     bool flag1 = false,flag2 = false;
     for (int i = 0;i < ans.size ();i++)
     {
         if (ans[i] == oppose [0])
         {
              flag1 = true;
         }
         if (ans[i] == oppose [1])
         {
              flag2 = true;
         }
     }
     if (flag1 && flag2)
     {
         ans.clear ();
     }
}                           

int main ()
{
    int test;
    cin>>test;
    for (int testid = 1; testid <=test;testid++)
    {
        vector <string> trans;
        vector <string> oppose;
        vector <char> elelist;
        string element;
        string temp;
        int C,D,N;
        cin>>C;
        for (int i = 0;i<C;i++)
        {
            cin>>temp;
            trans.push_back (temp);
        }
        cin>>D;    
        for (int i = 0;i<D;i++)
        {
            cin>>temp;
            oppose.push_back (temp);
        }
        vector <char> ans;
        cin>>N;
        cin>>element;
        ans.push_back (element[0]);
        for (int i=1;i<N;i++)
        {
            ans.push_back (element[i]);
            for (int j= 0;j<C;j++)
            {
                transform (ans,trans[j]);
            }        
            for (int j = 0;j<D;j++)
            {
                checkoppose (ans,oppose[j]);
            }
        }
        //cout <<ans.size()<<endl;
        cout<<"Case #"<<testid<<": [";
        if (ans.size () == 0)
        {
           cout<<"]"<<endl;
        }
        else
        {   
        for (int i = 0;i < ans.size () - 1;i++)
        {
            cout<<ans[i]<<", ";
        }
        cout<<ans[ans.size() - 1]<<"]"<<endl;
        }
    }
    return 0;
}                     
