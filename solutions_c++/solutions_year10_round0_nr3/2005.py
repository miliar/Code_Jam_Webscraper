// GCJ2010Q3.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include "stdlib.h"


int _tmain(int argc, _TCHAR* argv[])
{
	long long int T=0;
	long long int R=0,k=0,N=0;
	long long int i=0,j=0,j_temp=0;
	long long int j_limit=0;
	long long int g[2010];
	int c;
	long long int case_count=0;
	long long int ans=0,ans_temp=0;
	char data[100];
	long long int data_count=0;
	long long int DCG[2010][4];//有向有閉路グラフ？ 有向無閉路グラフ＝ＤＡＧなので // [1]次の順番へ、[2]それまでに乗る人＝１回当たりの金額
	//R>Nのときはかならず閉路を持つ
	long long int DCG_count=0;
	long long int DCG_count_now=0;
	long long int cycle_count=0;
	long long int DCG_value=0;
	long long int i2=0;
	long long int DCG_check=0;
	long long int loop=0,mod_loop=0;
	int ch=0;
	FILE *fp1,*fp2;
	fp1=fopen("C-large.in","r");
	fp2=fopen("C-large.out","w");
	fscanf(fp1,"%d",&T);
	while(T!=0){
		T--;
		case_count++;
		j=0;
		j_temp=0;
		fscanf(fp1,"%d %d %d",&R,&k,&N);

		for(i=0;i<=N+10;i++){
			DCG[i][1]=-1;
			DCG[i][2]=0;
		}
		DCG[1][1]=1;//開始時は常に１番目の人から始まるので
		DCG_count=0;
		DCG_count_now=0;
		cycle_count=0;
		DCG_value=0;
		DCG_check=0;
		loop=0;
		mod_loop=0;
		ch=0;
		for(i=0;i<=N;i++){
			data_count=0;
			while ( (c=fgetc(fp1)) != EOF){
				data[data_count]=c;
				data_count++;
				if(c==' '||c=='\n'){
					g[i]=atol(data);
					break;
				}
			}
			//printf("i=%d	g[i]=%d\n",i,g[i]);//g[0]は改行コードになってしまう、困った。
		}
		g[N+1]=g[1];
		ans=0;
		ans_temp=0;
		j=1;
		j_temp=1;
		j_limit=N+1; //並んでる列が全部なくなるとき C-small-attempt0.inの７番目をまちがえたためj_limit=1からj_limit=N+1に変更
		for(i=1;i<=R;i++){
			for(j=j_temp;;j++){
				//printf("j=%d	j_temp=%d	ans_temp=%d\n",j,j_temp,ans_temp);
				ans_temp = ans_temp+g[j];
				if(j>N){	//j=N+1のときと同じ意味？
					j=1;
					//g[N+1]=g[1]にしたので影響を与えないはず。
				}
				if(ans_temp+g[j+1] > k || j+1==j_limit || N==1){
					j_temp=j+1;
					break;
				}
			}
			j_limit=j_temp;

			if(j_limit==N+1 && i==1){
				ans=R*ans_temp;
				break;
			}

			if(DCG_check==0){
				DCG_count_now=DCG_count_now+1;
				DCG[DCG_count_now+1][1]=j_temp;
				DCG[DCG_count_now][2]=ans_temp;
				//printf("	ans_temp=%ld\ntemp=%ld",ans_temp,j_temp);
				for(DCG_count=1;DCG_count<DCG_count_now;DCG_count++){
					if(DCG[DCG_count_now][1]==DCG[DCG_count][1]){//閉路が完成
						//printf("閉路完成	DCG_count_now=%lld	DCG_count=%lld\n",DCG_count_now,DCG_count);
						for(i2=1;i2<=DCG_count_now;i2++){
							//printf("i2=%lld	DCG[i2][1]=%lld	DCG[i2][2]=%lld\n",i2,DCG[i2][1],DCG[i2][2]);	
						}
						DCG[DCG_count_now+2][1]=1;
						DCG[DCG_count_now+1][2]=ans_temp;
						loop=DCG_count_now-DCG_count;
						DCG_check=1;
						
						for(i2=DCG_count;i2<DCG_count_now;i2++){
							//printf("順番%ld　金額%ld	次%ld\n",i2,DCG[i2][2],DCG[i2][1]);
							DCG_value=DCG_value+DCG[i2][2];
						}
						//printf("(DCG_count_now-DCG_count)=%ld　(R-i)=%ld	DCG_value=%ld\n",loop,(R-i),DCG_value);
						//printf("iの加算%ld　金額の加算%ld\n",(R-i)/(DCG_count_now-DCG_count),(R-i)/(DCG_count_now-DCG_count)*DCG_value);
						ans=ans+(R-i)/(DCG_count_now-DCG_count)*DCG_value;
						mod_loop=(R-i)%(DCG_count_now-DCG_count);
						i=R-mod_loop;
						//printf("閉路終了後	i=%ld　金額=%ld\n",i,ans);
					}
				}
			}
			ans = ans + ans_temp;
			//printf("%d回目	その回の料金＝%d	合計料金=%d\n",i,ans_temp,ans);
			ans_temp=0;

		}
		//printf("\n");
		//printf("Case #%lld: %lld\n",case_count,ans);
		fprintf(fp2,"Case #%lld: %lld\n",case_count,ans);	
		//if(DCG_check==1){fprintf(fp2,"	閉路あり\n");}
		//else{fprintf(fp2,"	閉路なし\n");}
	}
	return 0;
}

