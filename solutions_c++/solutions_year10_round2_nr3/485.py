# include <iostream>

using namespace std;

int array [50][50];

int cons (int a,int b)
{
    int ans=0;
    if (a < b)
    {
        return 0;
    }
    if (b == 1)
    {
        return 1;
    }    
    if (a==b)
    {
         return 1;
    }
    ans = cons (a-1,b) + cons (a-1,b-1);
    ans = ans % 100003;
    return ans;
}                      

int main ()
{
    int test;
    cin>>test;
    int index = 1;
    while (index <=test)
    {
        int N;
        cin>>N;
        memset (array,0,sizeof(array));
        for (int i=2;i<=N;i++)
        {
            array[i][1] = 1;
            for (int j=2;j<=N;j++)
            {
                  if (j >=i)
                  {
                        array[i][j] = 0;
                  }
                  else
                  {
                        for (int k = 1;k < j;k++)
                        {
                            array [i][j] +=((array[j][k]) * cons(i-j,j-k));
                            array[i][j] = array[i][j]%100003;
                        }
                  }
            }
        }               
        int ans = 0;
        for (int i=1;i<=N;i++)
        {
            ans+= (array[N][i]);
            ans= ans % 100003;                      
        }
        cout<<"Case #"<<index<<": "<<ans<<endl;
        index++;
    }
    return 0;
}
               
