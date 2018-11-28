#include <stdio.h>

int main() {
    long long t,tt,r,k,n,i,j,c,q,kk,qq,kkk,a[1111],w[1111],p[1111],mark[1111];
    FILE *ff=fopen("C-large.in","r"), *gg=fopen("C-large1.out","w");

    fscanf(ff,"%I64lld", &tt);
    for(t=1; t<=tt; t++) {

        fscanf(ff,"%I64lld%I64lld%I64lld", &k, &r, &n);
        for(i=1; i<=n; i++) fscanf(ff,"%I64lld", &a[i]);

        for(i=1; i<=n; i++) {
           mark[i]=0;
           j=i; w[i]=0; p[i]=0;
           while (w[i]+a[j]<=r) {
              w[i]+=a[j]; p[i]++;
              j++; if (j>n) j=1;
              if (j==i) break;
           }
        }

        c=0; q=1; kkk=0;
        while (k) {
           //mark[q]=kkk;
           c+=w[q];
           q+=p[q]; if (q>n) q-=n;
           k--; kkk++;
           //if (mark[q]) {
           //  qq=q;
           //  kk=kkk-mark[q]+1;
           //  break;
           //}
        }
      if (k>0 && kk>0) {
        c = c + (k/kk) * c;
        k=k%kk;
        q=qq;
        while (k) {
           c+=w[q];
           q+=p[q]; if (q>n) q-=n;
           k--;
        }
      }
        fprintf(gg,"Case #%I64lld: %I64lld\n", t, c);
    }

    fclose(ff); fclose(gg);
    return 0;
}
