#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

int getat(const vector<int> &a, int x) {
    return (x<0||x>=(int)a.size()) ? 0 : a[x];
}
int &getrat(vector<int> &a, int x) {
    while(x>=(int)a.size())a.push_back(0);
    return a[x];
}
void normalize(vector<int> &a) {
    for(int j = 0; j+1 < (int)a.size(); j++) {
        while(a[j]<0) {
            a[j]+=10;
            a[j+1]--;
        }
        while(a[j]>=10) {
            a[j]-=10;
            a[j+1]++;
        }
    }
    while(!a.empty() && a.back()==0)a.pop_back();
}

void setdiff(vector<int> &a, const vector<int> &b) {
    bool gte = true;
    int n = max((int)a.size(), (int)b.size());
    for(int j = 0; j < n; j++) {
        int aj = getat(a,j);
        int bj = getat(b,j);
        if(aj==bj)continue;
        gte = aj>bj;
    }
    for(int j = 0; j < n; j++) {
        getrat(a,j) -= getat(b,j);
        if(!gte)getrat(a,j) *= -1;
    }
    normalize(a);
}
void setmod(vector<int> &a, const vector<int> &b) {
    for(int i = a.size()-b.size(); i>=0; i--) {
        while(true) {
            bool gte = true;
            int n = max((int)a.size(), (int)b.size()+i);
            for(int j = 0; j < n; j++) {
                int aj = getat(a,j);
                int bj = getat(b,j-i);
                if(aj==bj)continue;
                gte = aj>bj;
            }
            if(!gte)break;
            for(int j = 0; j < n; j++) {
                getrat(a,j) -= getat(b,j-i);
            }
            normalize(a);
        }
    }
}
void setgcd(vector<int> &x, vector<int> &y) {
    while(!y.empty()) {
        setmod(x,y);
        x.swap(y);
    }
}

int main(int argc, char **argv) {
    int c; scanf("%d", &c);
    for(int i = 0; i < c; i++) {
        int n; scanf("%d", &n);
        vector<vector<int> > nums(n);
        for(int j = 0; j < n; j++) {
            static char str[60];
            scanf("%s", str);
            for(int k = strlen(str)-1; k >= 0; k--) {
                nums[j].push_back(str[k]-'0');
            }
            normalize(nums[j]);
        }
        for(int j = 1; j < n; j++) {
            setdiff(nums[j], nums[0]);
        }
        for(int j = 2; j < n; j++) {
            setgcd(nums[1], nums[j]);
        }
        setmod(nums[0],nums[1]);
        setdiff(nums[0],nums[1]);
        if(nums[0]==nums[1])nums[0].clear();
        if(nums[0].empty())nums[0].push_back(0);
        printf("Case #%d: ", i+1);
        for(int j = nums[0].size()-1; j >= 0; j--) {
            printf("%c", (char)('0'+nums[0][j]));
        }
        printf("\n");
    }
    return 0;
}

