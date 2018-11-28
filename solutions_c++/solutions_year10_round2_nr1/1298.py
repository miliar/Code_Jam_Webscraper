#include "stdio.h"
#include "conio.h"

int T, N, M, total_mkdir_commands;
char curr_paths[10000][200];
char make_paths[10000][200];


int is_directory_present( char *path_ptr )
{
int i, j, match;

for( i=0; i<N; i++ )
 {
	match = true;
	for( j=0; j<200; j++ )
	 {
		if( path_ptr[j] != curr_paths[i][j] )
		 {
			match = false;
			break;
		 }
		if( path_ptr[j] == 0 )
			break;
	 }
	if( match )
		return true;
 }
return false;
}


int mkdir( char *path_ptr )
{
int i;

for( i=0; i<200; i++ )
 {
	curr_paths[N][i] = path_ptr[i];
	if( path_ptr[i] == 0 )
		break;
 }
N++;
total_mkdir_commands++;
}



int main()
{
int i, j, t;
FILE *in_ptr, *out_ptr;

in_ptr = fopen( "A-large.in", "r+" );
if( in_ptr == NULL ) { printf( "Giris dosyasi acilamadi...\n" ); return 0; }

out_ptr = fopen( "A-small.out", "w+" );
if( out_ptr == NULL ) { printf( "Cikis dosyasi acilamadi...\n" ); return 0; }

fscanf( in_ptr, "%d", &T );

for( t=1; t<=T; t++ )
 {
	fscanf( in_ptr, "%d", &N );
	fscanf( in_ptr, "%d", &M );

	for( i=0; i<N; i++ )
		fscanf( in_ptr, "%s", &curr_paths[i][0] );

	for( i=0; i<M; i++ )
		fscanf( in_ptr, "%s", &make_paths[i][0] );

	total_mkdir_commands = 0;
	for( i=0; i<M; i++ )
	 {
		int num_of_dirs, temp_dirs, dir_level;
		char temp_path[200];

		num_of_dirs=0; j=0; dir_level=0;
		while( make_paths[i][j] )
		 {
			if( make_paths[i][j] == '/' )
				num_of_dirs++;
			j++;
		 }

		while( num_of_dirs )
		 {
			temp_dirs = num_of_dirs+1;
			j = 0;

			while( temp_dirs )
			 {
				temp_path[j] = make_paths[i][j];
				if( temp_path[j] == '/' )
					temp_dirs--;
				if( temp_path[j++] == 0 )
					break;
			 }
			temp_path[j-1] = 0;
			//printf( "%s\n", &temp_path[0] );

			if( is_directory_present( &temp_path[0] ) )
			 {
				dir_level = num_of_dirs;
				break;
			 }
			num_of_dirs--;
		 }
		//printf( " Dir_level = %d\n", dir_level );

		int curr_dir_level;

		curr_dir_level=-1; j=0;
		while( true )
		 {
			temp_path[j] = make_paths[i][j];

			if( temp_path[j] == '/' )
			 {
				curr_dir_level++;
				if( curr_dir_level > dir_level )
				 {
					temp_path[j] = 0;
					mkdir( &temp_path[0] );
					temp_path[j] = '/';
				 }
			 }

			if( temp_path[j] == 0 )
			 {
				curr_dir_level++;
				if( curr_dir_level > dir_level )
				 {
					temp_path[j+1] = 0;
					mkdir( &temp_path[0] );
				 }
				break;
			 }
			j++;
		 }
	 }
	printf( "Case %d : Total MKDIR Commands = %d\n", t, total_mkdir_commands );
	fprintf( out_ptr, "Case #%d: %d\n", t, total_mkdir_commands );

 }
fclose( out_ptr );
fclose( in_ptr );
return 0;
}