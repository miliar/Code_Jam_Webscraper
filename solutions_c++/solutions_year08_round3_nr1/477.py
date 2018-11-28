# include <iostream>
# include <algorithm>
# include <vector>

using namespace std;
int main ()
{
    vector <int> nums,num2;
    int cases;
    int keys,max,tot,num,temp=0,hill=0;
    cin>>cases;
    long long ret=0;
    for (int i=0;i<cases;i++)
    {
        cin>>max;
        cin>>keys;
        cin>>tot;
	nums.clear ();
	num2.clear ();
        temp=0;
        hill=0;
        ret=0;
        for (int j=0;j<tot;j++)
        {
            cin>>num;         
            nums.push_back (num);
        }
        sort (nums.begin(),nums.end());
        for (int k=nums.size ()-1;k>=0;k--)
        {
            num2.push_back (nums[k]);
        }    
        while (temp!=num2.size ())
        {
              if (temp%keys==0)
                 hill++;
              ret+=(hill*num2[temp]);
              temp++;
        }        
        cout<<"Case #"<<i+1<<": "<<ret<<endl;
    }
    return 0;
}    
        
                                      
