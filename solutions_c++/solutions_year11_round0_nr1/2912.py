
#include <stdio.h>
using namespace std;

typedef enum {B, O} Robot_enum;
typedef struct Position_struct Position;

struct Position_struct {
  Robot_enum robot;
  int button;
  bool met;
  Position *next;
  Position *next_b;
  Position *next_o;
};

class BotTrust {
  private:
    Position *sequence;
    Position *b_events;
    Position *o_events;
    Position *last_sequence;
    Position *last_b_events;
    Position *last_o_events;

    int result;
  public:
    BotTrust() {
      sequence = NULL;
      b_events = NULL;
      o_events = NULL;
      last_sequence = NULL;
      last_b_events = NULL;
      last_o_events = NULL;

      result = 0;
    }

    ~BotTrust() {
      Position *c = NULL, *n = NULL;
      c = sequence;
      while (c) {
	n = c->next;
	delete c;
	c = n;
      }
    }

    void addPosition(Robot_enum r, int button) {
      Position *p = new Position();
      p->robot = r;
      p->button = button;
      p->met = false;
      p->next = NULL;
      p->next_b = NULL;
      p->next_o = NULL;

      if (!sequence) {
	sequence = p;
	last_sequence = sequence;
      }
      else {
	last_sequence->next = p;
	last_sequence = p;
      }

      if (r == B) {
	if (!b_events) {
	  b_events = p;
	  last_b_events = b_events;
	}
	else {
	  last_b_events->next_b = p;
	  last_b_events = p;
	}
      }
      if (r == O) {
	if (!o_events) {
	  o_events = p;
	  last_o_events = o_events;
	}
	else {
	  last_o_events->next_o = p;
	  last_o_events = p;
	}
      }
    }

    void computeSteps() {
      Position *s = sequence;
      Position *b = b_events;
      Position *o = o_events;
      int b_count = 1;
      int o_count = 1;

      while (s) {
	if (b) {
	  if (s == b) {
	    if (s->button == b_count) {
	      // push button
	      s->met = true;
	      b = b->next_b;
	    }
	    else {
	      // move towards button
	      b_count += (s->button > b_count) ? 1 : -1;
	    }
	  }
	  else {
	    if (b->button == b_count) {
	      // stay put
	    }
	    else {
	      // move towards button
	      b_count += (b->button > b_count) ? 1 : -1;
	    }
	  }
	}
	if (o) {
	  if (s == o) {
	    if (s->button == o_count) {
	      // push button
	      s->met = true;
	      o = o->next_o;
	    }
	    else {
	      // move towards button
	      o_count += (s->button > o_count) ? 1 : -1;
	    }
	  }
	  else {
	    if (o->button == o_count) {
	      // stay put
	    }
	    else {
	      // move towards button
	      o_count += (o->button > o_count) ? 1 : -1;
	    }
	  }
	}

	if (s->met) s = s->next;
	++result;
      }
    }

    void print(FILE *fp) {
      Position *p = sequence;

      fprintf(fp, "Sequence: ");
      while (p) {
	fprintf(fp, "(%c, %d)", (p->robot == B) ? 'B' : 'O', p->button);
	p = p->next;
      }
      fprintf(fp, "\n");

      p = b_events;
      fprintf(fp, "B Events: ");
      while (p) {
	fprintf(fp, "(%c, %d)", (p->robot == B) ? 'B' : 'O', p->button);
	p = p->next_b;
      }
      fprintf(fp, "\n");

      p = o_events;
      fprintf(fp, "O Events: ");
      while (p) {
	fprintf(fp, "(%c, %d)", (p->robot == B) ? 'B' : 'O', p->button);
	p = p->next_o;
      }
      fprintf(fp, "\n");
    }

    void printResult(FILE *fp) {
      fprintf(fp, "%d", result);
    }
};

void skipWS(FILE *fp)
{
  char s[1024];
  fscanf(fp, "%[ \t\n]", s);
}

int main(int argc, char **argv)
{
  FILE *infile = NULL, *outfile = NULL;
  int numtests = 0, i = 0, j = 0;
  BotTrust *bots = NULL;

  if (argc != 2) {
    printf("Usage %s <input_file>\n", argv[0]);
    return -1;
  }

  infile = fopen(argv[1], "r");
  if (!infile) {
    printf("Cannot find file %s\n", argv[1]);
    return -1;
  }

  outfile = fopen("result.out", "w");
  if (!outfile) {
    printf("Cannot open output file result.out for writing.\n");
    fclose(infile);
    return -1;
  }

  fscanf(infile, "%d", &numtests);
  if (numtests <= 0) {
    fclose(infile);
    fclose(outfile);
    return 0;
  }

  bots = new BotTrust[numtests];
  for (i = 0; i < numtests; i++) {
    int numpos, b;
    char r;

    skipWS(infile);
    fscanf(infile, "%d", &numpos);
    for (j = 0; j < numpos; j++) {
      skipWS(infile);
      fscanf(infile, "%c", &r);
      skipWS(infile);
      fscanf(infile, "%d", &b);
      bots[i].addPosition((r == 'B') ? B : O, b);
    }
  }
  fclose(infile); infile = NULL;

  for (i = 0; i < numtests; i++) {
    bots[i].computeSteps();

    fprintf(outfile, "Case #%d: ", i + 1);
    bots[i].printResult(outfile);
    fprintf(outfile, "\n");
#if 0
    /* Test */
    bots[i].print(stdout);
#endif
  }

  delete [] bots;

  fclose(outfile);
  return 0;
}

