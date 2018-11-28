#include<iostream>
#include<cmath>

using namespace std;

struct elem{
	char c;
	int bot;
	bool cli;
};
int main()
{
	int tcase;
	int n,pi;
	char ch;
	int bt,ot;
	int o_pos,b_pos;
	int temp,temp1;
	elem ob[105],bb[105];
	elem *(p[105]);
	int top1,top2;
	int nexto,nextb;
	int i;
	int walk = 0;
	FILE *in,*out;
    in = freopen("A-large.in","r",stdin);
    out = freopen("A-large.txt","w",stdout);
	cin >>tcase;
	while(tcase--){
	    cin >>n;
		top1 = top2 = 0;
		ob[0].bot = 1; ob[0].cli = true;
		bb[0].bot = 1; bb[0].cli = true;
		for(i = 0;i < n;i++){
		    cin >>ch >>pi;
			if(ch == 'O'){
				p[i] = &ob[top1];
				ob[top1].c = ch;
				ob[top1].cli = true;
				ob[top1++].bot = pi;
			}
			if(ch == 'B'){
				p[i] = &bb[top2];
				bb[top2].c = ch;
				bb[top2].cli = true;
				bb[top2++].bot = pi;
			}
		}
		bt = ot = 0;
		b_pos = o_pos = 1;
		nexto = nextb = 0;
		temp1 = 0;
		for(i = 0;i < n;i++){
			if(p[i]->c == 'O'){
				temp = abs(p[i]->bot-o_pos);
				ot += temp+1;
				o_pos = p[i]->bot;
				nexto++;
				p[i]->cli = false;
				if((bb[nextb-1].cli && b_pos == bb[nextb].bot) || nextb == top2){
					bt += temp+1;
				}
				else{
					if(temp+1 < (temp1 = abs(bb[nextb].bot-b_pos))){
						b_pos = b_pos+(bb[nextb].bot > b_pos? (temp+1):(-temp-1));
						bt += temp+1;
					}
					else{
						b_pos = bb[nextb].bot;
						bt += temp+1;
						//nextb++;
					}
				}
			}
			if(p[i]->c == 'B'){
				temp = abs(p[i]->bot-b_pos);
				bt += temp+1;
				b_pos = p[i]->bot;
				nextb++;
				p[i]->cli = false;
				if((ob[nexto-1].cli && o_pos == ob[nexto].bot) || nexto == top1){
					ot += temp+1;
				}
				else{
					if(temp+1 < (temp1 = abs(ob[nexto].bot-o_pos))){
						o_pos = o_pos+(ob[nexto].bot > o_pos? (temp+1):(-temp-1));
						ot += temp+1;
					}
					else{
						o_pos = ob[nexto].bot;
						ot += temp+1;
						//nexto++;
					}
				}
			}//cout <<"o_pos:" <<o_pos <<' '<<ot <<"b_pos:" <<b_pos <<' '<<bt <<endl;
		}
		if(p[n-1]->c == 'O')
			cout << "Case #" << ++walk <<": "<< ot <<endl;
		else cout << "Case #" << ++walk <<": "<<bt <<endl;
	}
fclose(in);
	fclose(out);
	return 0;
}