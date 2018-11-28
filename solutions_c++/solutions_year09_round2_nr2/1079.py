# include <iostream>
# include <vector>
# include <algorithm>

using namespace std;

int main ()
{
    vector <int> val;
    int test;
    cin>>test;
    int j=1;
    while (test--)
    {
          string n;
          cin>>n;
          val.clear ();
          for  (int i=0;i<n.size ();i++)
          {
                val.push_back (n[i]-'0');
          }
          //reverse (val.begin (),val.end ());
          next_permutation (val.begin (),val.end ());
          string ans;
          for (int i=0;i<val.size();i++)
          {
                   ans.push_back (val[i]+'0');
                   //ans+=val[i];
          }
          vector <int>::iterator it;
          it=val.begin ();
          it++;
          if (ans<=n)
          {
                   sort (val.begin (),val.end ());
                   int k=0;
                   while (val[k]==0)
                   {
                         k++;
                   }
                   val[0]=val[k];
                   if (k!=0) val[k]=0;
                   val.insert (it,1,0);
                   ans="";
                   for (int i=0;i<val.size ();i++)
                   {
                       ans.push_back (val[i]+'0');
                       //ans+=val[i];
                   }    
          }                
          cout<<"Case #"<<j<<": "<<ans<<endl;
          j++;
    }
    return 0;
}    
          
