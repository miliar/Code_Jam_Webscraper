
 #include <iostream>
 #include <stdio.h>
 
 using namespace std;
 
 int main() {
    
    FILE* fp = fopen("Csmall.in","r");  
    FILE* fp1 = fopen("c.out","w");
    
    long t1,t2,t3;
    int n;
    
    fscanf(fp,"%d\n",&n);
    
    for(int var=0;var<n;var++) 
    {    
    
    cout<<"\r Processing "<<var;     
         
    fscanf(fp,"%ld %ld %ld\n",&t1,&t2,&t3);
    
    const long no_groups=t3,R=t1, K=t2;    
 
    long* groups; 
    
    groups = new long[no_groups];
    
    for(int gvar=0; gvar<no_groups; gvar++)
            fscanf(fp,"%ld ",&groups[gvar]);     
                
    long pindex=0,euro_count = 0;
    
    long index;
    
    index=pindex;         
      
    for(long i=0;i<R;i++) {     
    
    long count=0, t; 
    while(true) {                        
       
       if( (t=count + groups[index]) <= K ) 
        count = t;        
       else {
        pindex = index;      
        break;     
       } 
       index = (index+1)%no_groups;      
       if(index==pindex) break;            
     }            
      euro_count += count;       
    }  
    
    delete[] groups;    
    
    fprintf(fp1,"Case #%d: %ld\n",var+1, euro_count);  

}   
    
    
    fclose(fp);
    fclose(fp1);
    
    cout<<"\n Done ";
    
    char c;
    cin.get(c);     
      
    return 0;  
  }
