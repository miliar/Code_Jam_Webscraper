#include<stdio.h>
#include<conio.h>

long int arr[1000];
long int no_of_candies;
long int candies1[1000];
long int candies2[1000];
long int find_the_division()
{
  long int check = 0,length = 0,small = 0;
  int l = 0;
  small = arr[0];
  for(int i = 0;i < no_of_candies;i++)
  {
     check = check ^ arr[i];
     if(arr[i] < small)
     {
       small = arr[i];
     }
  }
  long int sum = 0;
  for(i = 0; i < no_of_candies;i++)
  {
   sum = sum + arr[i];
  }
  sum = sum - small;
  if(check != 0)
  {
    return 0;
  }
  else
  {
   return sum;
  }



}

int main()
{
    freopen("candy.txt" ,"r+",stdin);
    freopen("candyout.txt" ,"w+",stdout);
    int num_of_cases = 0;
    scanf("%d",&num_of_cases);
    for(int i=0;i<num_of_cases;i++)
    {
     scanf("%d\n",&no_of_candies);
    for(long int j = 0;j<no_of_candies;j++)
     {
      scanf("%ld ",&arr[j]);
      }
     long int value= find_the_division();
    if(!value)
    {
      printf("Case #%d: NO\n",i+1);
    }
    else
    {
      printf("Case #%d: %ld\n",i+1,value);
    }

    }
     fclose(stdin);
    fclose(stdout);
}