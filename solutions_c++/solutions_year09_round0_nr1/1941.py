 #include <conio.h>
 #include <stdio.h>
 #include <string.h>
 #define fi "A-large.in"
 #define fo "A-large.out"

 typedef char string15[15];
 typedef unsigned int arr[500][15];


 int i,j,h,D,L,K,N,o,save[500];
 char str[500];
 arr dd1,dd2;
 /*********************/
 void turn_on_bit(unsigned int &num,int i){
      num=(num | (1<<i));
 }
 /*********************/
 void turn_off_bit(unsigned int &num,int i){
      num=num & (~(1<<i));
 }
 /*********************/
 int get_bit(unsigned int &num,int i){
     return (num>>i) & 1;
 }
 /**********************/
 void init(int N){
 int i,j;
	for (i=0;i<N;i++)
		for (j=0;j<15;j++){
			dd1[i][j]=0;
			dd2[i][j]=0;
		}
 }
 /**********************/
 void readfile(){
 int j;
 FILE *f=fopen(fi,"rt");
 fscanf(f,"%d %d %d",&L,&D,&N);
 for (i=0;i<D;i++){
	fscanf(f,"%s",str);
 }
	init(N);
 for (i=0;i<N;i++){
	fscanf(f,"%s",str);
	j=0;
	o=0;
	h=0;
	 while (h<strlen(str)){
	    if (str[h]=='(') o=1;
	    if ( (str[h]!='(') && (str[h]!=')') ){
	       if (str[h]-'a'<16)
		   turn_on_bit(dd1[i][j],str[h]-'a');
		   else turn_on_bit(dd2[i][j],str[h]-'a'-16);
	    }
	    if (o==0) j++; else
	    if (str[h]==')')  {j++;o=0;}
	    h++;
	}
 }
 fclose(f);
 }
 /************************/
 void writefile(){
 int i,j,h;
 FILE *g=fopen(fo,"wt");
 FILE *f=fopen(fi,"rt");

 fscanf(f,"%d %d %d",&L,&D,&N);
 for (i=0;i<N;i++) save[i]=0;
 for (i=0;i<D;i++){
	fscanf(f,"%s",str);
     for (j=0;j<N;j++){
	o=0;
	for (h=0;h<L;h++){
	      if  (str[h]-'a'<16){
		  if (get_bit(dd1[j][h],str[h]-'a')==1) o++;
	      } else
	      if (get_bit(dd2[j][h],str[h]-'a'-16)==1) o++;
	}
	if (o>=L) save[j]++;
     }
 }
 for (i=0;i<N;i++)
 {
	fprintf(g,"Case #%d: %d\n",i+1,save[i]);
 }
 fclose(f);
 fclose(g);
 }
/**************/
 void main()
 {
 clrscr();
 readfile();
 writefile();
 }