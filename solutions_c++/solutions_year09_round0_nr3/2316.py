OUT=welcome
OBJS=welcome.o

#CPPFLAGS=-Wall -g
CPPFLAGS=-O3

build: $(OUT)

$(OUT): $(OBJS)
	$(LINK.cc) -o $@ $<

clean:
	$(RM) $(OUT) $(OBJS)

all: clean build
