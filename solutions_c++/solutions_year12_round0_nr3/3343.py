#include<iostream>
//#include<math.h>
int arr[8];
 
/*int queue(int temp)
{
    int k=0;
    while(temp)
    {
      arr[k] = temp%10;
      temp = temp/10;
      k++;
               }
      return *arr;
    }
  */  
void rotate(int arr[],const int count)
{
    const int first_element = arr[0];
    for(int index=0; index < count; index++)
    {
       arr[index] = arr[index + 1];
       
            }
       arr[count - 1] = first_element;
    }
  void display(int* arr, const int count) {
    for (int index = 0; index < count; ++index)
        printf("%d  ", *(arr + index));
    printf("\n"); 
}  
/*int rotate(int a)
{   
    int temp1=a;
    int d=1;
    while(temp1)
    {
       d = d*10;
       temp1 = temp1/10;
            }
       
       d = d/10;
       return (a%(d))*10 + a/d;
    }*/
int main()
{
  int T,n=1,A,B,i=0,k=0,temp=0,num=0,cnt=0;
  scanf("%d",&T);
  getchar();
  while(T--)
  {
   scanf("%d %d",&A,&B);
   printf("Case #%d: ",n++);
   temp = A;
   int c=0;
    cnt=0;
   while(temp)
   {
     temp = temp/10;
     c++;
           }
   for(i=A;i<=B;i++)
   {   temp = i;
      // arr = queue(temp);
        
        
        int k=0;
    while(temp)
    {
      arr[k] = temp%10;
      temp = temp/10;
      k++;}
      //cnt++;         }
      //display(arr,c);
        
        
        
                    //num = i;
     // temp = i;
      //int c = 0;
     for(int p=0;p<c;p++)
     {
      rotate(arr,c);
      //display(arr,c);
      num = 0;
      for(k=(c-1);k>=0;k--)
      {//printf("%d\n",arr[k]);
                      //int p = pow(10,k);
                      num = num*10 + arr[k];
     
      }
       //printf("%d\n",num);
      if((num<=B)&&(num>i))
      {//printf("hi");
      cnt++;
       }      }           
                    }
   
   
      printf("%d",cnt);
      printf("\n");      } 
      
      //system("pause"); 
    }
 