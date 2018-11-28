
#include<cstdio>
#include<iostream>
#include<string>

#define MAX_DIGITS 12

int digits[MAX_DIGITS];
int digits_count;

int num_digits(int value)
{
  digits_count = 0;
  while(value)
  {
    digits[digits_count++] = value%10;
    value = value/10;
  }
  return digits_count;
}

int get_number(int index)
{
  int i,value=0;
  for(i=(digits_count-1);i>=0;i--)
  {
    value = value * 10;
    if((i+index) < digits_count)
    { 
      value += digits[i+index];
    }
    else
    {
      value += digits[i+index-digits_count];
    }
  }
  return value;
}

int main(void)
{
  int test_count,A,B,temp;
  int i,j,k;
  int count=0;
  int output_value=0;

  //Read test count
  scanf("%d",&test_count);
  
  for(k=0;k<test_count;k++)
  {
    output_value = 0;
    //Read integers
    scanf("%d %d", &A, &B);
 
    for(i=A;i<=B;i++)
    {
      count = num_digits(i);
      //printf("Count: %d\n",count);
      for(j=1;j<count;j++)
      {
        temp = get_number(j);
        if(temp > i)
        {
          if(temp <= B)
          {
            //Found the pair
            output_value++;
            //printf("Index %d: %d, %d\n",output_value,i,temp);
          }
        }
      }  
    }
    printf("Case #%d: %d\n",k+1,output_value);
  }
  return 0;
}


