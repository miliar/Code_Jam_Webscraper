#include<iostream>
#include<new>
using namespace std;
int comp(int *c,int n)
{int ans=0;
for(int l=0;l<n;l++)
{
    ans=ans^c[l];
}
return ans;
}
void q_sort(int numbers[], int left, int right)
{
  int pivot, l_hold, r_hold;

  l_hold = left;
  r_hold = right;
  pivot = numbers[left];
  while (left < right)
  {
    while ((numbers[right] >= pivot) && (left < right))
      right--;
    if (left != right)
    {
      numbers[left] = numbers[right];
      left++;
    }
    while ((numbers[left] <= pivot) && (left < right))
      left++;
    if (left != right)
    {
      numbers[right] = numbers[left];
      right--;
    }
  }
  numbers[left] = pivot;
  pivot = left;
  left = l_hold;
  right = r_hold;
  if (left < pivot)
    q_sort(numbers, left, pivot-1);
  if (right > pivot)
    q_sort(numbers, pivot+1, right);
}
void quickSort(int numbers[], int array_size)
{
  q_sort(numbers, 0, array_size - 1);
}
int main()
{
int t,n,*c;

cin>>t;
for(int i=1;i<=t;i++)
{
cin>>n;
c=new int[n];
for(int k=0;k<n;k++)
cin>>c[k];
quickSort(c,n);
int r=comp(c,n);
if(r==0)
{
  int sum=0;
  for(int j=1;j<n;j++)
  sum=sum+c[j];
  cout<<"Case #"<<i<<": "<<sum<<"\n";
}
else
cout<<"Case #"<<i<<": NO\n";
delete []c;
}
return 0;
}
