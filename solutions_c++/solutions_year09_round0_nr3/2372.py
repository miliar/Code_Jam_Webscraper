#include <stdio.h>

char tem[] = {'w','3','l','8','0','6','4','A','t','1','B','9','2','d','5','C','j','a','7'};
int mic[1000];
int ans;
FILE *fp;
FILE *fw;
int main(){
    int n,index;
    char c;
    char s[4000];
    fp = fopen("C-small-attempt0.in","r");
    fw = fopen("Welcome.out","w");
    fscanf(fp,"%d",&n);
    fscanf(fp,"%c",&c);
    printf("%d",n);
    for(int z=0;z<n;z++){
            index = 0;
            fscanf(fp,"%c",&c);
            while(c != '\n'){
                    if(c == 'o'){
                         s[index++] = '0';
                         s[index++] = '1';
                         s[index++] = '2';
                    }else if(c == 'e'){
                         s[index++] = '3';
                         s[index++] = '4';
                         s[index++] = '5';
                    }else if(c == 'm'){
                         s[index++] = '6';
                         s[index++] = '7';
                    }else if(c == 'c'){
                         s[index++] = '8';
                         s[index++] = '9';
                    }else if(c == ' '){
                         s[index++] = 'A';
                         s[index++] = 'B';
                         s[index++] = 'C';
                    }else
                         s[index++] = c;
                    fscanf(fp,"%c",&c);
            }

            while(s[index-1] != '7' && index > 1)
            index--;
            
            if(index >17){
            mic[index-1] = 1;
      
            
            for(int i=0;i<index;i++){
            if(s[i] == '7') mic[i] = 1;
            else mic[i] = 0;
            }
            for(int i = index-1;i>=0;i--){
                    for(int j = 0;j < 18;j++){
                            if(s[i] == tem[j]){
                                      for(int k=i+1;k< index;k++){
                                              if(s[k] == tem[j+1]){
                                                      mic[i] += mic[k]; 
                                              }
                                      }
                            }
                    }
                    mic[i] %= 10000;
            }/*
                    for(int i = 0;i<index;i++){
                          printf("%3c ",s[i]);
                    }
                    printf("\n");
                    for(int i = 0;i<index;i++){
                          printf("%3d ",mic[i]);
                    }
                    printf("\n");
*/
                    ans = 0;
                    for(int i = 0;i<index;i++){
                            if(s[i] == 'w'){
                            ans+=mic[i];
                            ans%=10000;
                            }
                    }
                    
                    fprintf(fw,"Case #%d: %d%d%d%d\n",z+1,(ans/1000)%10,(ans/100)%10,(ans/10)%10,ans%10);
            }
            else{
                 fprintf(fw,"Case #%d: 0000\n",z+1);
            } 
    }
    fclose(fp);
    fclose(fw);

return 0;
}
