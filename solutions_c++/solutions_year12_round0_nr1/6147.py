#include <iostream>
#include <cstdio>
#include <map>
#include <vector>
#include <cstdlib>
using namespace std;
int main() {
    freopen("A-small-attempt4.in","r",stdin);
    freopen("A-small.out","w",stdout);
    char s1[1000],s2[1000],s3[1000];
    map<char, char> m;
    strcpy(s1,"ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv");
    strcpy(s2,"ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup");
    for(int i=0; i<strlen(s1); i++) {
        m[s1[i]]=s2[i];
    }   
    m['z']='q';
    m['q']='z';
    m[' ']=' ';
    int t;
    cin >> t;
    getchar();
    for(int i=1; i<=t; i++) {
        gets(s3);
        printf("Case #%d: ",i);
        for(int i=0; i<strlen(s3); i++) 
            cout << m[s3[i]];
        printf("\n");
    }
    return 0;
}
