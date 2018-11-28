//      A.cpp
//      
//      Copyright 2011 Kushagra Gour a.k.a. Chin Chang <chinchang457@gmail.com>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <iostream>
#include <stdio.h>
#include <queue>

using namespace std;

int main(int argc, char** argv)
{
	FILE *f,*fo;
	f=fopen("A-large.in","r");
	fo=fopen("A_large_out.txt","w");
	int t,n;
	fscanf(f,"%d",&t);
	for(int test=1;test<=t;test++){
		fscanf(f,"%d ",&n); //cout<<n<<"#"<<endl;
		queue<int> o,b;
		int no=0,nb=0;
		int opos=1,bpos=1,ns=0;
		queue<char> seq;
		bool odone = true, bdone = true;
		
		for(int i=0;i<n;i++){
			char who;
			int button;
			
			// get all data into arrays 			
			fscanf(f,"%c %d ",&who,&button);
			
			if(who=='O'){ o.push(button); seq.push('O'); if(odone) odone=false; }
			else{ seq.push('B'); b.push(button); if(bdone) bdone=false;  }			
		}
		
		no = o.size();
		nb = b.size();
		
		
		// simulate now
		
		char turn = seq.front(); seq.pop();
		while(!odone || !bdone){
			bool switchTurn = false;
			if(!odone){
				if(o.front()>opos) { opos++; /*cout<<"\n o move to "<<opos;*/ }
				else if(o.front()<opos) { opos--; /*cout<<"\n o move to "<<opos;*/ }
				else if(turn == 'O'){ /*cout<<"\n o pressed "<<opos; */
					switchTurn = true;
					o.pop();
					if(o.empty()) odone = true;
				}
			}
			if(!bdone){
				if(b.front()>bpos) { bpos++; /*cout<<"\n B move to "<<bpos;*/ }
				else if(b.front()<bpos) { bpos--; /*cout<<"\n B move to "<<bpos;*/ }
				else if(turn == 'B'){ /*cout<<"\n B pressed "<<bpos;*/
					turn = seq.front(); seq.pop();
					b.pop();
					if(b.empty()) bdone = true;
				}
			}
			if(switchTurn) { turn = seq.front(); seq.pop(); }
			ns++; //cout<<"\n------";
		}
		
		fprintf(fo,"Case #%d: %d\n",test,ns);
		
	}
	fclose(f); fclose(fo);
	return 0;
}
