#include <cstdio>
#include <algorithm>

inline int max(int a, int b){
    return (a > b)? a: b;
}

inline int min(int a, int b){
    return (a < b)? a: b;
}

struct seg_t{

    int l, r, val, tmp;
    seg_t *lch, *rch;

    seg_t(int nl, int nr){
        lch = rch = NULL;
        l = nl, r = nr, val = 0, tmp = -1;
    }

    int qry(int ql, int qr){

        if((ql == l && qr == r) || tmp != -1) return val;
        else{
            if(!lch) return val;
            int m = (l + r) / 2;
            if(qr <= m) return lch->qry(ql, qr);
            else if(ql >= m) return rch->qry(ql, qr);
            else return max(lch->qry(ql, m), rch->qry(m, qr));
        }

    }

    void cover(int cl, int cr, int cv){

        if(cl == l && cr == r){
            val = cv, tmp = 1;
        }
        else{
            int m = (l + r) / 2;
            if(!lch){
                while(!lch) lch = new seg_t(l, m);
                while(!rch) rch = new seg_t(m, r);
            }
            if(tmp != -1){
                tmp = -1;
                lch->cover(l, m, val);
                rch->cover(m, r, val);
            }
            if(cr <= m) lch->cover(cl, cr, cv);
            else if(cl >= m) rch->cover(cl, cr, cv);
            else{
                lch->cover(cl, m, cv);
                rch->cover(m, cr, cv);
            }
            val = max(lch->val, rch->val);
        }

    }

    ~seg_t(){
        if(lch){
            delete lch;
            delete rch;
        }
    }

};

struct stu_t{

    int ind, r;

    bool operator < (const stu_t& cmp) const{
        return r < cmp.r;
    }

    void init(int nind){
        ind = nind;
        scanf("%d" ,&r);
    }

}stu[1010];

int ansX[1010], ansY[1010];

int main(){

    int t;
    scanf("%d" ,&t);

    for(int T = 1; T <= t; T++){

        int n, w, l;
        scanf("%d %d %d" ,&n ,&w ,&l);

        for(int i = 0; i < n; i++){
            stu[i].init(i);
        }

        std::sort(stu, stu + n);

        seg_t *root = NULL;
        while(root == NULL) root = new seg_t(0, w);
        for(int i = n - 1, rec = 0; i >= 0; i--){
            int r = stu[i].r;
            int ind = stu[i].ind;
            if(r + rec > w) rec = 0;
            int low = root->qry(rec, min(rec + r + r, w));
            ansY[ind] = (low == 0)? 0: low + r;
            if(rec == 0){
                ansX[ind] = 0;
                root->cover(0, min(r, w), ansY[ind] + r);
                rec = r;
            }
            else{
                ansX[ind] = rec + r;
                root->cover(rec, min(w, rec + r + r), ansY[ind] + r);
                rec = rec + r + r;
            }
            if(ansY[ind] > l) fprintf(stderr, "warn\n");
        }
        delete root;

        printf("Case #%d:" ,T);
        for(int i = 0; i < n; i++){
            printf(" %d %d" ,ansX[i] ,ansY[i]);
        }
        putchar('\n');

    }

}
