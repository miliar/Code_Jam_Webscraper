#include <cstdio>
#include <cstdlib>

char names[][99] = {"Sheldon", "Leonard", "Penny","Rajesh","Howard" };

int main(){
    long long base = 1;
    long long men = 5;
    int n;
    scanf("%d",&n);
    --n;
    while(1){
        if(n<base*men){
            printf("%s\n",names[n/base]);
            break;
        }else{
            n -= base*men;
            base = base * 2;
        }
    }
//    system("pause");
    return 0;
}
