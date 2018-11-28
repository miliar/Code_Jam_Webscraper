#include <stdio.h>
#include <string.h>

using namespace std;
 
void find_mapping(int a[]);
 
int main()
{
        int a[26];
        find_mapping(a);
        a[25] = 'q' - 'a';
 
        int t;
        scanf("%d", &t);
        char str[102];
		int k = 1;		
		char ch;
		scanf("%c", &ch);        

        while(t--)
        {
               fgets(str, 102, stdin);
                int l = strlen(str);
				printf("Case #%d: ", k);
                
                for (int i = 0; i < l - 1; i++)
                {
                        if (str[i] == ' ')
                        {
                                printf(" ");
                        }
                        else
                        {
                                printf("%c", a[str[i] - 'a'] + 'a');
                        }
                }

				printf("\n");
				k++;
        }
        
        
        
        return 0;
}
 
void find_mapping(int a[])
{
        char s1[] = "our language is impossible to understand";
        char s2[] = "there are twenty six factorial possibilities";
        char s3[] = "so it is okay if you want to just give up";
        
        char s1_r[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
        char s2_r[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
        char s3_r[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
        
        a['y' - 'a'] = 'a' - 'a';
        a['e' - 'a'] = 'o' - 'a';
        a['q' - 'a'] = 'z' - 'a';
        
        int l1 = strlen(s1);
        int l2 = strlen(s2);
        int l3 = strlen(s3);
        
        for (int i = 0; i < l1; i++)
        {
                if (s1_r[i] != ' ')
                {
                        a[s1_r[i] - 'a'] = s1[i] - 'a';
                }
        }
        
        for (int i = 0; i < l2; i++)
        {
                if (s2_r[i] != ' ')
                {
                        a[s2_r[i] - 'a'] = s2[i] - 'a';
                }
        }
        
        for (int i = 0; i < l3; i++)
        {
                if (s3_r[i] != ' ')
                {
                        a[s3_r[i] - 'a'] = s3[i] - 'a';
                }
        }
}
