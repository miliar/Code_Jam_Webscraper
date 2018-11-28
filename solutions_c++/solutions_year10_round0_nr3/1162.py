#include <stdio.h>

struct g_table
{
    int gi;
    unsigned long total; 
    int next;
};

g_table group[1000];

void main()
{
    FILE *fp1,*fp2;
    
    fp1 = fopen("c.in.txt", "r");
    fp2 = fopen("c.out.txt", "w+");

    int t;
    fscanf(fp1, "%d", &t);

    for (int i=1; i<=t; i++)
    {
        unsigned long r,k,n;
        fscanf(fp1, "%lu %lu %lu", &r, &k, &n);
        
        for (unsigned long j=0; j<n; j++)
        {
            unsigned long gi;
            fscanf(fp1, "%d", &gi);
            group[j].gi = gi;
            group[j].total = 0;
            group[j].next = -1;
        }

        long long total = 0;
        int pos = 0;
        for (unsigned long j=0; j<r; j++)
        {
            if (group[pos].next != -1 && group[pos].total != 0)
            {
                // »º´æ
                total += group[pos].total;
                pos = group[pos].next;
            }
            else
            {
                // ¼ÆËã
                int last_pos = pos;
                int count = 0;
                unsigned max_num = 0;
                
                while (count < n && max_num + group[pos].gi <= k)
                {
                    max_num += group[pos].gi;
                    count++;
                    pos = (pos+1) % n;
                }

                group[last_pos].next = pos;
                group[last_pos].total = max_num;

                total += group[last_pos].total;
            }
        }

        fprintf(fp2, "Case #%d: %lld\n", i, total);
    }

    fclose(fp1);
    fclose(fp2);
}