#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct BIG{
	int num[65];
	int digit;
}A,B,zero,data[1005];
BIG mul(BIG &a,int m){
	BIG c;
	memset(c.num,0,sizeof(c.num));
	int carry=0,i,j,flag;
	for(i=0;i<a.digit;i++){
		c.num[i] += a.num[i]*m;
	}
	for(i=0;i<a.digit;i++){
		c.num[i]+=carry;
		carry =  c.num[i]/10;
		c.num[i] %= 10;
	}
	c.digit = a.digit;
	if(carry > 0){
		c.num[c.digit] = carry;
		c.digit++;
	}
	flag = 0;
	for(i = c.digit;i>=0;i--){
		if(c.num[i] != 0){
			flag = 1;
			c.digit = i+1;
			break;
		}
	}
	if(flag == 0)c.digit = 1;
	return c;	
}
int comp(BIG &a,BIG &b){
	int i;
	if(a.digit>b.digit)return 1;
	if(a.digit<b.digit)return -1;
	for(i=a.digit-1;i>=0;i--){
		if(a.num[i] > b.num[i])return 1;
		if(a.num[i] < b.num[i])return -1;
	}
	return 0;
}
BIG minus(BIG &a,BIG &b){
	BIG c;
	c.digit = 1;
	int i,j;
	memset(c.num,0,sizeof(c.num));
	if(comp(a,b) == 1){
		i = a.digit-1;
		while(i >= 0){

			if(a.num[i] < b.num[i]){
				j = i+1;
				while(c.num[j] == 0){
					c.num[j] = 9;
					j++;
				}
				c.num[j]--;
				c.num[i] = a.num[i]+10 - b.num[i];
			}
			else{
				c.num[i] = a.num[i] - b.num[i];
			}
			i--;
		}
		for(i=a.digit;i>=0;i--){
			if(c.num[i]!=0){
				c.digit = i+1;
				break;
			}
		}
	}
	else{
		i = b.digit-1;
		while(i >= 0){
			if(b.num[i] < a.num[i]){
				j = i+1;
				while(c.num[j] == 0){
					c.num[j] = 9;
					j++;
				}
				c.num[j]--;
				c.num[i] = b.num[i]+10 - a.num[i];
			}
			else{
				c.num[i] = b.num[i] - a.num[i];
			}
			i--;
		}
		for(i=b.digit;i>=0;i--){
			if(c.num[i]!=0){
				c.digit = i+1;
				break;
			}
		}
	}
	return c;
}
BIG divide(BIG &a,BIG &b){
	BIG tmp,ans,tmp2,tmp3;
	int d = a.digit,i,j,pos;
	pos = a.digit - b.digit+1;
	memset(ans.num,0,sizeof(ans.num));
	ans.digit = pos;
	pos--;
	if(comp(a,b)==0){ans.digit = 1;ans.num[0]=1;a = minus(a,b);};
	while(comp(a,b) > 0){
		memset(tmp.num,0,sizeof(tmp.num));
		for(i=d-1,j=b.digit-1;i>=0,j>=0;i--,j--){
			tmp.num[i] = b.num[j];
		}
		tmp.digit = d;
		for(i=0;i<10;i++){
			tmp2 = mul(tmp,i);
			tmp3 = mul(tmp,i+1);
			if(comp(a,tmp2) >= 0 && comp(a,tmp3) < 0){
				ans.num[pos] = i;

				pos--;
				break;
			}
		}
		a = minus(a,tmp2);
		d--;
	}
	for(i=ans.digit;i>=0;i--){
		if(ans.num[i] != 0)
		{
			ans.digit = i+1;
			break;
		}
	}
	return ans;
}
BIG mulbig(BIG a,BIG b){
	int i,j,carry;
	BIG c;
	memset(c.num,0,sizeof(c.num));
	for(i=0;i<a.digit;i++){
		for(j=0;j<b.digit;j++){
			c.num[i+j] += a.num[i] * b.num[j];
		}
	}
	carry = 0;
	for(i=0;i<a.digit+b.digit;i++){
		c.num[i] += carry;
		carry = c.num[i] / 10;
		c.num[i] %= 10;
	}
	for(i=a.digit+b.digit;i>=0;i--){
		if(c.num[i] != 0){
			c.digit = i+1;
			break;
		}
	}
	return c;
}
BIG plus(BIG a,BIG b){
	BIG c;
	memset(c.num,0,sizeof(c.num));
	int i=0,carry,d;
	while(i < a.digit || i < b.digit){
		c.num[i] += a.num[i] + b.num[i];
		i++;
	}
	carry = 0;
	for(i=0;i<a.digit+1 || i < b.digit+1 ;i++){
		c.num[i] += carry;
		carry = c.num[i]/10;
		c.num[i] %= 10;
	}
	if(a.digit > b.digit)d = a.digit+1;
	else d = b.digit+1;
	for(i = d; i >= 0 ;i--){
		if(c.num[i] != 0){
			c.digit = i+1;
			break;
		}
	}
	return c;
}
BIG GCD(BIG &a,BIG &b){
    BIG tmp,tmp2,aa,bb;
    int i;
    memset(aa.num,0,sizeof(aa.num));
    memset(bb.num,0,sizeof(bb.num));
    for(i=0;i<=a.digit;i++)
        aa.num[i] = a.num[i];
    aa.digit = a.digit;
    for(i=0;i<=b.digit;i++)
        bb.num[i] = b.num[i];
    bb.digit = b.digit;
    if(comp(a,b) == 0)return aa;
    while(1){
        if(comp(bb,zero) == 0 || comp(aa,zero) == 0)break;
        tmp = divide(aa,bb);
        tmp2 = aa;
        aa = bb;
        bb = tmp2;

    }
    return aa;
}
int main (){
	int i,flag,j,T,n,z,ca,flag2,y;
	char s[1005],ch;
	BIG tmp,ans,tmp2,one;
	scanf("%d",&T);
	memset(zero.num,0,sizeof(zero.num));zero.digit = 1;zero.num[0] = 0;
	memset(one.num,0,sizeof(one.num));one.digit = 1;one.num[0] = 1;
	for(ca = 1;ca <= T; ca++){
        scanf("%d",&n);
        flag =0;
        tmp2.digit = 1;tmp2.num[0] = 1;
        for(z=0;z<n;z++){
            memset(data[z].num,0,sizeof(data[z].num));
            flag2 = 0;
		    scanf("%s",s);

        	for(i=0;i<strlen(s);i++){
        		if(s[i] != '0'){j = i;break;}
        	}
        	for(i=strlen(s)-1;i>=j;i--){
        		data[z].num[(strlen(s)-1) - i] = s[i]-48; 
        	}
        	data[z].digit = strlen(s)-j;
            if(z > 0){
                tmp = minus(data[z],data[z-1]);

                if(flag == 0 && comp(tmp,zero) != 0){
                     tmp2 = tmp;
                     flag = 1;
                }
                else{

            		if(comp(tmp,zero) != 0)
                    tmp2 = GCD(tmp2,tmp);
                   
                }
            }
        }
        tmp = divide(data[0],tmp2);
        if(comp(zero,data[0]) !=0)
            ans = minus(tmp2,data[0]);
        else
            ans = data[0];
        printf("Case #%d: ",ca);
		for(i=ans.digit-1;i>=0;i--){
				printf("%d",ans.num[i]);
		}
		printf("\n");
	}

	return 0;
}
