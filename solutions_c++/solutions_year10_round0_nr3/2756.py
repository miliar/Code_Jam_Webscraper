#include <sys/types.h> 
#include <sys/stat.h> 
#include <fcntl.h> 
#include <stdio.h> 
#include <math.h> 
#include <string.h>
#include <stdlib.h> 
#include <iostream>
using namespace std;

#define MAXDIGITS 500
#define PLUS 1
#define MINUS -1
#define max(a,b) ((a>b)?a:b)



typedef struct {
        char digits[MAXDIGITS]; /* represent the number */
        int signbit; /* 1 if positive, -1 if negative */
        int lastdigit; /* index of high-order digit */
} bignum;

int add_bignum(bignum *a, bignum *b, bignum *c);

void print_bignum(bignum *n, int caso)
{
     cout << "Case #"<< caso <<": "<<n->digits << endl;
     // printf("\n");
}
void int_to_bignum(int s, bignum *n)
{
      if (s >= 0) n->signbit = PLUS;
      else n->signbit = MINUS;
      int t = abs(s);
      sprintf(n->digits,"%d",t);
      n->lastdigit=strlen(n->digits);
}
void int_to_bignum(char *s, bignum *n)
{
      int i;
      if (s[0] != -1)
      {
         n->signbit = PLUS;
         i = 0;
      }
      else
      { 
        i = 1;
        n->signbit = MINUS;
      }
      strcpy(n->digits,&s[i]);
      n->lastdigit = strlen(n->digits);
}
void initialize_bignum(bignum *n)
{ 
     int_to_bignum(0,n); 
}



int compare_bignum(bignum *a, bignum *b)
{
    int i; /* counter */
    if ((a->signbit == MINUS) && (b->signbit == PLUS)) return(PLUS);
    if ((a->signbit == PLUS) && (b->signbit == MINUS)) return(MINUS);
    if (b->lastdigit > a->lastdigit) return (PLUS * a->signbit);
    if (a->lastdigit > b->lastdigit) return (MINUS * a->signbit);
    for (i = 0; i < a->lastdigit; i++ )
    {
        if (a->digits[i] > b->digits[i]) return(MINUS * a->signbit);
        if (b->digits[i] > a->digits[i]) return(PLUS * a->signbit);
    }
    return(0);
}

int subtract_bignum(bignum *a, bignum *b, bignum *c)
{
    int borrow; /* has anything been borrowed? */
    int v; /* placeholder digit */
    register int i,j,op=0; /* counter */
    int n_borrow;
    int temp;
    c->signbit = PLUS;
    if ((a->signbit == MINUS) || (b->signbit == MINUS))
    {
         b->signbit = -1 * b->signbit;
         n_borrow = add_bignum(a,b,c);
         b->signbit = -1 * b->signbit;
         return n_borrow;
    }
    if (compare_bignum(a,b) == PLUS)
    {
         n_borrow = subtract_bignum(b,a,c);
         c->signbit = MINUS;
         return n_borrow;
    }
    
    int k = c->lastdigit = max(a->lastdigit,b->lastdigit);
    n_borrow=0;
    c->digits[k--]='\0';
    for(i=a->lastdigit-1,j=b->lastdigit-1;j>=0;i--,j--)
    {
         temp = a->digits[i]-'0'-( b->digits[j]-'0'+op);
         if(temp < 0)
         {
             temp += 10;
             op=1;
             n_borrow++;
         }
         else op=0;
         c->digits[k--]= temp+'0';
    }    
    while(op)
    {
         temp = a->digits[i--]-op-'0';
         if(temp < 0)
         {
             temp += 10;
             op=1;
             n_borrow++;
         }
         else op=0;
         c->digits[k--]= temp+'0';
    }
    
    for(;i>=0;i--)
         c->digits[k--]=a->digits[i];

    for(i=0;!(c->digits[i]-'0');i++);
    
    c->lastdigit = c->lastdigit - i;
    
    if(i==a->lastdigit)
        strcpy(c->digits,"0");
    else
    {
        char string[MAXDIGITS];
        strcpy(string,&c->digits[i]);
        strcpy(c->digits,string);
    }
    
    return n_borrow;
}





int add_bignum(bignum *a, bignum *b, bignum *c)
{
     int carry; /* carry digit */
     int i,j,op=0;; /* counter */
     int n_carry,temp;
     initialize_bignum(c);
     if (a->signbit == b->signbit)
        c->signbit = a->signbit;
     else
     {
         if (a->signbit == MINUS)
         {
            a->signbit = PLUS;
            n_carry = subtract_bignum(b,a,c);
            a->signbit = MINUS;
         }
         else
         {
            b->signbit = PLUS;
            n_carry = subtract_bignum(a,b,c);
            b->signbit = MINUS;
         }
     return n_carry;
     }
     
     if(a->lastdigit < b->lastdigit)
           return add_bignum(b,a,c);
     int k = c->lastdigit = a->lastdigit+1;
     c->digits[k--]='\0';
     carry = 0;
     n_carry = 0;
     for(i=b->lastdigit-1,j=a->lastdigit-1;i>=0;i--,j--)
     {
        carry = b->digits[i]-'0'+a->digits[j]-'0'+carry;
        c->digits[k--]= (carry%10)+'0';
        carry=carry/10;
        if(carry)
                 n_carry++;
     }
     for(;j>=0;j--)
     {
         carry = a->digits[j]-'0'+carry;
         c->digits[k--] = (carry % 10)+'0';
         carry = carry/10;
         if(carry)
                  n_carry++;
     }
     if(carry)
           c->digits[k]=carry+'0';
     else
     {
           char string[MAXDIGITS];
           strcpy(string,&c->digits[1]);
           strcpy(c->digits,string);
           c->lastdigit=c->lastdigit - k - 1;
     }
     return n_carry;
}

void multiply_bignum(bignum *a, bignum *b, bignum *c)
{
    long int n_d;
    register long int i,j,k;
    short int num1[MAXDIGITS],num2[MAXDIGITS],of=0,res[MAXDIGITS]={0};
    n_d=(a->lastdigit<b->lastdigit)?b->lastdigit:a->lastdigit;
    n_d++ ;
    for(i=0,j= a->lastdigit-1;i< a->lastdigit ;i++,j--)
         num1[i]=a->digits[j]-48;
    for(i=0,j= b->lastdigit-1;i< b->lastdigit ;j--,i++)
         num2[i]=b->digits[j]-48;
    res[0]=0;
    for(j=0;j< b ->lastdigit;j++)
    { 
         for(i=0,k=j;i< a->lastdigit || of;k++,i++)
         { 
              if(i<a->lastdigit)
                     res[k] += num1[i] * num2[j] + of;
              else res[k] += of;
              of=res[k]/10;
              res[k]=res[k]%10;
         }
    }
    
    for(i=k-1,j=0;i>=0;i--,j++)
         c->digits[j]=res[i]+48;
    
    c->digits[j]='\0';
    c->lastdigit=k;
    c->signbit = a->signbit*b->signbit;
}

void copy(bignum *a, bignum *b)
{
    a->lastdigit=b->lastdigit;
    a->signbit = b->signbit;
    strcpy(a->digits,b->digits);
}

void divide_bignum(bignum *n1,bignum *n2,bignum *n3,bignum *n4)
{
    initialize_bignum(n3);
    bignum a,b,temp;
    a.signbit=b.signbit=temp.signbit=PLUS;
    int asign = n1->signbit;
    n1->signbit = PLUS;
    int bsign = n2->signbit;
    n2->signbit = PLUS;
    temp.lastdigit=0;
    int_to_bignum(1,&b);
    copy(&a,n1);
    while(compare_bignum(&a,n2)<1)
    {
         subtract_bignum(&a,n2,n4);
         add_bignum(n3,&b,&temp);
         copy(&a,n4);
         copy(n3,&temp);
    }

    n1->signbit = asign;
    n2->signbit = bsign;
    n3->signbit = n1->signbit * n2->signbit;
    if(n4->digits[0] !='0')
           n4->signbit = asign;
}







long long int arrayN[2000];
    
    long long int T;
    long long int k;
    long long int R;
    long long int N;
    
    
bignum simular()
{
        long long int i=0;
        long long int ultsub=0;
        long long int primsub=0;
        long long int primvez=0;
        
        long long int dentro=0;
        
        bignum res;
        bignum tmp1;
        bignum tmp2;
        
        
        initialize_bignum(&res);
        
        while(i<R)
        {
            if((arrayN[ultsub]+dentro)<=k && (primsub!=ultsub || primvez==0) )
            {
                primvez=1;
                dentro=dentro+arrayN[ultsub];
                ultsub++;
                if(ultsub>=N)
                    ultsub=0;
            }
            else
            {
                primvez=0;
                copy(&tmp1,&res);
                int_to_bignum(dentro, &tmp2);
                add_bignum(&tmp1,&tmp2,&res);
                
                i++;
                dentro=0;
                primsub=ultsub;
            }
            
        }
        return res;
        
}

int main()
{
    
    
    
    
    long long int i,j,x;
    
    
          close (0); open ("a.in", O_RDONLY); 
          close (1); open ("a.out", O_WRONLY | O_CREAT, 0600); 
    cin >> T;
    
    for(i=0;i<T;i++)
    {
        cin >> R;
        cin >> k;
        cin >> N;
        
        for(j=0;j<N;j++)
        {
            cin >> arrayN[j];
        }
        
        bignum res=simular();
        print_bignum(&res, i+1);
        
    }
    
    
}
