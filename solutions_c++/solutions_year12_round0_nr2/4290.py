#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
int a[100],b[100],c[100],p,T[100];
bool all_under_p(int a ,int b , int c , int p);
void func(int T,int p,int danc_c);
bool norm(int a , int b , int c);
bool norm_2(int a , int b , int c);
void sefr(){int uu = 0; for(uu = 0 ; uu < 100 ; uu++){a[uu] = 0;b[uu] = 0;c[uu]=0;p = 0;T[uu] =0; }}
int max(int a);
int main()
{
    int TT,i,dancer_n,dancer_c,sup_n;
    cin >> TT;
    for(i = 0 ; i < TT;i++)
    {
        sefr();
        cin >> dancer_n>>sup_n>>p; // input first 3
        for(dancer_c  = 0 ; dancer_c<dancer_n;dancer_c++)// input T dancers
        {
            cin >>T[dancer_c];
        }

        //sort
        int mmm = 0;
        for(dancer_c  = 0 ; dancer_c<dancer_n;dancer_c++)// input T dancers
        {
            mmm = dancer_c;
            for(int yy = dancer_c ; yy<dancer_n;yy++)
            {
                if(T[yy]>T[mmm]) mmm = yy;
            }
            //swap
            int temppp = T[mmm];
            T[mmm] = T[dancer_c];
            T[dancer_c] = temppp;
        }


        for(dancer_c  = 0 ; dancer_c<dancer_n;dancer_c++)
        {
            func(T[dancer_c],p,dancer_c);
            //cout <<a[dancer_c]<<b[dancer_c]<<c[dancer_c]<<"\n";
        }
        //hame be surate behine hesab shodan
        int s_i,s_j;

      /*  for(s_i = 0 ; s_i < dancer_n ; s_i++)
        {
            for(s_j = s_i ; s_j < dancer_n ; s_j++)
            {
                int temp_a,temp_b,temp_c,temp_t;

                if(max(s_i)<max(s_j))
                {
                    temp_a=a[s_i];a[s_i] = a[s_j];a[s_j] = temp_a;
                    temp_b=b[s_i];b[s_i] = b[s_j];b[s_j] = temp_b;
                    temp_c=c[s_i];c[s_i] = c[s_j];c[s_j] = temp_c;
                    temp_t=T[s_i];T[s_i] = T[s_j];T[s_j] = temp_t;
                }
            }
        }*/



        while(sup_n > 0)
        {
            int flag = 0;
            // begardam unaE ke hame zir p an age normal 2 buddorostesh konam va 1y ham be sup ezafe she 1 flag ham bayad dashte bashe
            for(dancer_c  = 0 ; dancer_c<dancer_n;dancer_c++)
            {
                if(all_under_p(a[dancer_c],b[dancer_c],c[dancer_c],p))
                {// agar doroste age dar mode 2 e dorost beshe
                    // bayad bar asase bozorgtarine har goruh sort beshan
                    int a_temp,b_temp,c_temp;
                    a_temp = a[dancer_c];
                    b_temp = b[dancer_c];
                    c_temp = c[dancer_c];

                    if((a_temp>=b_temp)&&(a_temp>=c_temp)){a_temp++;if(b_temp<c_temp){c_temp--;}else{b_temp--;} }else{
                    if((c_temp>=b_temp)&&(c_temp>=a_temp)){c_temp++;if(b_temp<a_temp){a_temp--;}else{b_temp--;} }else{
                    if((b_temp>=a_temp)&&(b_temp>=c_temp)){b_temp++;if(a_temp<c_temp){c_temp--;}else{a_temp--;} }}}
                    if(norm_2(a_temp,b_temp,c_temp)){a[dancer_c] = a_temp;b[dancer_c]=b_temp;c[dancer_c]=c_temp;sup_n--;flag = 1;}
                    if(sup_n == 0)goto here;
                }
            }
            if(flag == 0)goto here;//chizi nist ke beshe estefade kard
        }//shomaresh tedad va chap
        here:;
        int cunter = 0;
        for(dancer_c  = 0 ; dancer_c<dancer_n;dancer_c++)
            {
                //cout <<a[dancer_c]<<b[dancer_c]<<c[dancer_c]<<"\n";
              if(!all_under_p(a[dancer_c],b[dancer_c],c[dancer_c],p)){cunter++;}
            }
     cout <<"Case #"<<i+1<<": "<<cunter<<"\n";


    }

    return 0;
}
void func(int T,int p,int danc_c)
{
    if((T- p) >0){a[danc_c] = p;T = T-p;}
    if((T- p) >0){b[danc_c] = p;T = T-p;}
    c[danc_c] = T;
    while(norm(a[danc_c],b[danc_c],c[danc_c]) == false)
    {
        if((a[danc_c]>=b[danc_c])&&(a[danc_c]>=c[danc_c])){
                            a[danc_c] = a[danc_c]-1;if(b[danc_c]<c[danc_c]){b[danc_c] = b[danc_c]+1;}else {c[danc_c] = c[danc_c]+1;}
                          }else{
        if((c[danc_c]>=b[danc_c])&&(c[danc_c]>=a[danc_c])){
                            c[danc_c] = c[danc_c]-1;if(b[danc_c]<a[danc_c]){b[danc_c] = b[danc_c]+1;}else {a[danc_c] = a[danc_c]+1;}
                          }else{
        if((b[danc_c]>=a[danc_c])&&(b[danc_c]>=c[danc_c])){
                            b[danc_c] = b[danc_c]-1;if(a[danc_c]<c[danc_c]){a[danc_c] = a[danc_c]+1;}else {c[danc_c] = c[danc_c]+1;}
                          }}}
    }
}
bool norm(int a , int b , int c)
{
    if (a < 0) return false;
    if (b < 0) return false;
    if (c < 0) return false;
    if(abs(a - b)>=2){return false;}
    if(abs(a - c)>=2){return false;}
    if(abs(c - b)>=2){return false;}
    return true;
}
bool norm_2(int a , int b , int c)
{
    if (a < 0) return false;
    if (b < 0) return false;
    if (c < 0) return false;
    if(abs(a - b)>2){return false;}
    if(abs(a - c)>2){return false;}
    if(abs(c - b)>2){return false;}
    return true;
}
bool all_under_p(int a ,int b , int c , int p)
{
    if((a<p)&&(b<p)&&(c<p)) return true;
    return false;
}
int max(int e)
{
    int ted[3],m,n,MAX;
    ted[0] = a[e];
    ted[1] = b[e];
    ted[2] = c[e];
    MAX = ted[0];
    for(m = 0 ; m<2 ; m++){
        for(n = m+1 ; n < 3 ; n++)
        {
            if(ted[n] > MAX) MAX = ted[n];
        }
    }
}
