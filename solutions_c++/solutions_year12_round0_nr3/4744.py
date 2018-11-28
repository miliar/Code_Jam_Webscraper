#include<iostream>
using namespace std;
string retStr(int num)
{
       string ret;
       while(num)
       {
                 ret+= 'a' + num%10;
                 num/=10;
       }
       return ret;
}
int main()
{
      freopen ("C-small-attempt1.in","r",stdin);
     freopen ("myfile8888.txt","w",stdout);
 
    int T;
    cin>>T;
 
 
    for(int TN = 1; TN<= T;TN++)
    {
            int A,B;
            cin>>A>>B;
            int cnt=0;
            for(int m =A;m<=B;m++)
            {
                    for(int n= A;n<m;n++)
                    {
                            string str1 = retStr(m);
                            string str2 = retStr(n);
                            str1 += str1;
                            size_t found;

   
                            found=str1.find(str2);
                             if (found!=string::npos)
                            {
                                cnt++;
                            }
                    }
            }
            
            cout<<"Case #"<<TN<<": "<<cnt<<endl;
 
    }
    
     
   
    return 0;
}
