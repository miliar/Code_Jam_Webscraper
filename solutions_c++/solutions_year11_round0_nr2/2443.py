#include <cstdio>
#include <vector>
char Combine[256][256];
bool Oppose[256][256];
std::vector<char> List;
unsigned int i, j, k, T, N, Count[256];
char Str[1024];
char Temp;
int main(){
    scanf("%u", &T);
    for(i=0;i<T;i++){
        for(j=0;j<256;j++) for(k=0;k<256;k++){
            Combine[j][k]=0;
            Oppose[j][k]=0;
        }
        scanf("%u", &N);
        for(j=0;j<N;j++){
            scanf("%s", Str);
            Combine[Str[0]][Str[1]]=Str[2];
            Combine[Str[1]][Str[0]]=Str[2];
        }
        scanf("%u", &N);
        for(j=0;j<N;j++){
            scanf("%s", Str);
            Oppose[Str[0]][Str[1]]=1;
            Oppose[Str[1]][Str[0]]=1;
        }
        scanf("%u", &N);
        scanf("%s", Str);
        List.clear();
        for(k=0;k<256;k++) Count[k]=0;
        for(j=0;j<N;j++){
            if(!List.empty()){
                if(Combine[List.back()][Str[j]]!=0){
                    Temp=List.back();
                    Count[Temp]--;
                    List.pop_back();
                    List.push_back(Combine[Temp][Str[j]]);
                    Count[Combine[Temp][Str[j]]]++;
                }else{
                    for(k=32;k<128;k++){
                        if(Count[k]!=0&&Oppose[k][Str[j]]){
                            List.clear();
                            for(k=0;k<256;k++) Count[k]=0;
                            k=0;
                            break;
                        }
                    }
                    if(k==128){
                        List.push_back(Str[j]);
                        Count[Str[j]]++;
                    }
                }
            }else{
                List.push_back(Str[j]);
                Count[Str[j]]++;
            }
        }
        printf("Case #%u: [", i+1);
        if(!List.empty()){
            putchar(List[0]);
            for(j=1;j<List.size();j++){
                printf(", %c", List[j]);
            }
        }
        printf("]\n");
    }
    return 0;
}
