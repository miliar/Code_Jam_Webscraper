/* Tomasz [Tommalla] Zakrzewski, Google Code Jam 2011 /
/  Round 1B, Problem A */
 #include <cstdio>
 
 char matrix[110][110];
 double WP[110], OWP[110], OOWP[110], won[110], qty[110];
 
 int main()
 {
     unsigned int t, testId, n, i, j;
     double q;
     
     scanf("%u", &t );
     for( testId = 1; testId <= t; ++testId )
     {
	 printf("Case #%u:\n", testId);
	 scanf("%u", &n);
	 
	 for( i = 0; i < n; ++i )
	 {
	     scanf("%s", matrix[i] );
	     for( won[i] = qty[i] = j = 0; j < n; ++j )
		 if( matrix[i][j] != '.' )
		 {
		     qty[i] ++;
		     if( matrix[i][j] == '1' )
			 won[i]++;
		 }
		 
		 WP[i] = won[i]/qty[i];
	 }
	 
	 for( i = 0; i < n; ++i )
	 {
	     OWP[i] = q = 0.0;
	     for( j = 0; j < n; ++j )
		 if( i!=j && matrix[i][j] != '.' )
		 {
		     ++q;
		     OWP[i] += (won[j]-(matrix[i][j]=='0'))/(qty[j]-(matrix[i][j]!='.'));
		 }
		 
		 OWP[i]/=q;
	 }
	 
	 for( i = 0; i < n; ++i )
	 {
	     OOWP[i] = q = 0.0;
	     for( j = 0; j < n; ++j )
		 if( i != j && matrix[i][j] != '.' )
		 {
		     ++q;
		     OOWP[i] += OWP[j];
		 }
		 
		 OOWP[i] /= q;
	 }
	 
	 
	 for( i = 0; i < n; ++i )
	     printf("%lf\n", 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i] );
     }
     return 0;
 }