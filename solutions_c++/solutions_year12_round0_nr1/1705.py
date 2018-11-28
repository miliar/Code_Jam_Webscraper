char *a="yhesocvxduiglbkrztnwjpfmaq";
main(){
	int t,_,i;
	char s[999];
	scanf("%d",&_);gets(s);
	for(t=1; t<=_; t++){
		gets(s);
		printf("Case #%d: ",t);
		for(i=0; s[i]; i++)
			putchar(s[i]==' '?' ':a[s[i]-'a']);
		puts("");
	}
	return 0;
}

