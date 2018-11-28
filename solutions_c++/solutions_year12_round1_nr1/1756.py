#include<iostream>
using namespace std;

int main()
{
    int t,a,b,tmp,ptr=0,back=0,cas=1,i,j,c;
    float wrong[3];
    float prob[8];
    int key[8];
    int back1[8];
    int back2[8];
    int back3[8];
    int enter[8];
    float min=1000.0f,val=1.0f,sum_key=0,sum_back1=0,sum_back2=0,sum_back3=0,sum_enter=0;
    
    
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d",&a,&c);
        
        for(i=0;i<a;i++)
        {
            scanf("%f",&wrong[i]);                
        }          
        b=c-a;
        sum_key=0;
        sum_back1=0;
        sum_back2=0;
        sum_back3=0;
        sum_enter=0;
        min=1000.0f;
        
        for(i=0;i<(1<<a);i++)
        {
            tmp=i;
            ptr=a-1;
            val=1.0f;
            back=0;
            while(tmp>0)
            {
                if(tmp&1)
                {
                    val*=(1-wrong[ptr]);  
                }  
                else
                {
                    val*=wrong[ptr];
                }       
                ptr--; 
                back++;
                tmp=tmp>>1;
            }              
            while(ptr>=0)
            {
                val*=wrong[ptr];
                ptr--;             
            }       
            prob[i]=val;
            
            
                if(back==0)
                {
                    if(a==1)
                    {
                    key[i]=b+1;
                    back1[i]=b+3;
                    sum_key+=(key[i]*prob[i]);
                    sum_back1+=(back1[i]*prob[i]);
                    }
                    else if(a==2)
                    {
                    key[i]=b+1;
                    back1[i]=b+3;
                    back2[i]=b+5;
                    sum_key+=(key[i]*prob[i]);
                    sum_back1+=(back1[i]*prob[i]);
                    sum_back2+=(back2[i]*prob[i]);
                    }
                    else if(a==3)
                    {
                    key[i]=b+1;
                    back1[i]=b+3;
                    back2[i]=b+5;
                    back3[i]=b+7;
                    sum_key+=(key[i]*prob[i]);
                    sum_back1+=(back1[i]*prob[i]);
                    sum_back2+=(back2[i]*prob[i]);
                    sum_back3+=(back3[i]*prob[i]);
                    }          
                }                
                else if(back==1)
                {
                    if(a==1)
                    {
                    key[i]=b+1+a+b+1;
                    back1[i]=b+3;
                    sum_key+=(key[i]*prob[i]);
                    sum_back1+=(back1[i]*prob[i]);
                    
                    }
                    else if(a==2)
                    {
                    key[i]=b+1+a+b+1;
                    back1[i]=b+3;
                    back2[i]=b+5;
                    sum_key+=(key[i]*prob[i]);
                    sum_back1+=(back1[i]*prob[i]);
                    sum_back2+=(back2[i]*prob[i]);
                    
                    }
                    else if(a==3)
                    {
                    key[i]=b+1+a+b+1;
                    back1[i]=b+3;
                    back2[i]=b+5;
                    back3[i]=b+7;
                    sum_key+=(key[i]*prob[i]);
                    sum_back1+=(back1[i]*prob[i]);
                    sum_back2+=(back2[i]*prob[i]);
                    sum_back3+=(back3[i]*prob[i]);
                    }       
                }
                
                else if(back==2)
                {
                    if(a==1)
                    {
                    key[i]=b+1+a+b+1;
                    back1[i]=b+3+a+b+1;
                    sum_key+=(key[i]*prob[i]);
                    sum_back1+=(back1[i]*prob[i]);
                    
                    }
                    else if(a==2)
                    {
                    key[i]=b+1+a+b+1;
                    back1[i]=b+3+a+b+1;
                    back2[i]=b+5;
                    sum_key+=(key[i]*prob[i]);
                    sum_back1+=(back1[i]*prob[i]);
                    sum_back2+=(back2[i]*prob[i]);
                    
                    }
                    else if(a==3)
                    {
                    key[i]=b+1+a+b+1;
                    back1[i]=b+3+a+b+1;
                    back2[i]=b+5;
                    back3[i]=b+7;
                    sum_key+=(key[i]*prob[i]);
                    sum_back1+=(back1[i]*prob[i]);
                    sum_back2+=(back2[i]*prob[i]);
                    sum_back3+=(back3[i]*prob[i]);
                    }    
                }
                
                else if(back==3)
                {
                    if(a==1)
                    {
                    key[i]=b+1+a+b+1;
                    back1[i]=b+3+a+b+1;
                    sum_key+=(key[i]*prob[i]);
                    sum_back1+=(back1[i]*prob[i]);
                    
                    }
                    else if(a==2)
                    {
                    key[i]=b+1+a+b+1;
                    back1[i]=b+3+a+b+1;
                    back2[i]=b+5+a+b+1;
                    sum_key+=(key[i]*prob[i]);
                    sum_back1+=(back1[i]*prob[i]);
                    sum_back2+=(back2[i]*prob[i]);
                    
                    }
                    else if(a==3)
                    {
                    key[i]=b+1+a+b+1;
                    back1[i]=b+3+a+b+1;
                    back2[i]=b+5+a+b+1;
                    back3[i]=b+7;
                    sum_key+=(key[i]*prob[i]);
                    sum_back1+=(back1[i]*prob[i]);
                    sum_back2+=(back2[i]*prob[i]);
                    sum_back3+=(back3[i]*prob[i]);
                    }     
                }
                
                
                enter[i]=a+b+2;
                sum_enter+=(enter[i]*prob[i]);
                
        }
        min=sum_key;
        
        if(a==1)
        {
            if(min>sum_back1)
                min=sum_back1;
            if(min>sum_enter)
                min=sum_enter;        
        }
        else if(a==2)
        {
            if(min>sum_back1)
                min=sum_back1;
            if(min>sum_enter)
                min=sum_enter;
            if(min>sum_back2)
                min=sum_back2; 
        }
        else if(a==3)
        {
            if(min>sum_back1)
                min=sum_back1;
            if(min>sum_enter)
                min=sum_enter;
            if(min>sum_back2)
                min=sum_back2;
            if(min>sum_back3)
                min=sum_back3;     
        }
       
        printf("Case #%d: %f\n",cas++,min);
    }
        
        
        
}
