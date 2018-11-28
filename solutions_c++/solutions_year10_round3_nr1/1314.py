#include<iostream>
using namespace std;
int Partition(int low,int high,int arr[][2])
{ int i,high_vac,low_vac,pivot,pivot1,high_vac1,low_vac1/*,itr*/;
   pivot=arr[low][0];
   pivot1=arr[low][1];
   while(high>low)
{ high_vac=arr[high][0];
  high_vac1=arr[high][1];
  while(pivot<high_vac)
  {
    if(high<=low) break;
    high--;
    high_vac=arr[high][0];
    high_vac1=arr[high][1];
  }

  arr[low][0]=high_vac;
  arr[low][1]=high_vac1;
  low_vac=arr[low][0];
  low_vac1=arr[low][1];
  while(pivot>low_vac)
  {
    if(high<=low) break;
    low++;
    low_vac=arr[low][0];
    low_vac1=arr[low][1];
  }
  arr[high][0]=low_vac;
  arr[high][1]=low_vac1;
}
  arr[low][0]=pivot;
  arr[low][1]=pivot1;
   return low;
}

void Quick_sort(int low,int high,int arr[][2])
{
  int Piv_index,i;
  if(low<high)
  {
   Piv_index=Partition(low,high,arr);
   Quick_sort(low,Piv_index-1,arr);
   Quick_sort(Piv_index+1,high,arr);
  }
}

int main(){
    int t,kase;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for(kase=1;kase<=t;kase++)
    {
        int n,count=0;
        scanf("%d",&n);
        int points[n][2];
        for(int i=0;i<n;i++)
        {
            scanf("%d %d",&points[i][1],&points[i][0]);
        }
        /*for(int i=0;i<n;i++)
            cout<<points[i][0]<<" "<<points[i][1]<<endl;
        cout<<endl;*/
        Quick_sort(0,n-1,points);
        /*for(int i=0;i<n;i++)
            cout<<points[i][0]<<" "<<points[i][1]<<endl;*/
        for(int i=0;i<n;i++)
           for(int j=i;j<n;j++)
               if(points[i][1]>points[j][1])
                    count++;
         printf("Case #%d: %d\n",kase,count);

    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
