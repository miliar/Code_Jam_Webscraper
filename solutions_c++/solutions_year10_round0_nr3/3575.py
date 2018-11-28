#include<iostream>
using namespace std;
int main()
{
    int t , r,k ,n,*group,*group1,i=0,bpoint ,j,m,ppl,temp;
    int  count;
    cin >> t;
    while(i< t)
    {
             count =0;
             cin >> r >> k >> n;
             group = new int [n+1];
             group1= new int [n+1];
             for(j =0 ;j <n ;j ++)
             cin >> group[j];
             for(j=0 ;j < r ;j++)
             {
                     ppl=0;
                     for( m=0 ;m < n ;m ++)
                     {
                          ppl+= group[m];
                          if(ppl> k)
                          break;
                     }    
                     
                     if(m != n)
                     ppl -= group[m];
                     count += ppl;
                     
                     bpoint = m;
                     for(m = 0 ;m <n ;m++)
                     {
                           if(bpoint+m < n)
                           group1[m] = group[bpoint + m];
                           else
                           break;
                     }
                     bpoint = m;
                     temp=0;
                     for(m = bpoint ;m < n; m++)
                     {
                               group1[m] = group[temp];
                               temp++;
                     }
                    // group = group1;
                    for(m=0;m< n; m++)
                    group[m]=group1[m];
                   // cout << count <<"\n";
             }
             cout << "Case #"<<i+1<<": "<<count<<"\n";
             i++;
    }
   // system("pause");
    return 0;
}
                 
                           
                     
                     
    
