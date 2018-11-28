#include <cstdio>
#include <cstring>
#include <set>
using namespace std;
int numbercount(int number,int low) {
    set<int> numbers;
    char buf[50];
    sprintf(buf,"%d",number);
    int len = strlen(buf);
    for (int i = 0; i < len; ++i) {
        char c = buf[0];
        memmove(buf,buf+1,len - 1);
        buf[len-1] = c;
        int num = atoi(buf);
        if (low <= num && num < number) numbers.insert(num);
    }
    return numbers.size();
}
int process(int a, int b) {
    int sum = 0;
    for (int i = a; i <= b; ++i) {
        sum += numbercount(i,a); 
    }
    return sum;
}
int main(int argc, char* argv[]) {
    int lines;
    int a,b;
    scanf("%d",&lines);
    for (int i = 1; i <= lines; ++i) {
        scanf("%d %d",&a,&b);
        printf("Case #%d: %d\n",i,process(a,b));
    }
    return 0;
}
