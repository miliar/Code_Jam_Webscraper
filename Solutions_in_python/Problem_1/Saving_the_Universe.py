#!/usr/bin/python

import sys
import string
import sets
from optparse import OptionParser

## convenience class, store names and queries in-order
class DataSet:
	def __init__( self ):
		self.engines = []
		self.queries = []
	def __str__( self ):
		return "engines: %s\nqueries: %s" % ( str( self.engines ), str( self.queries ) )
	def n_engines( self ):
		return len( self.engines )
	def n_queries( self ):
		return len( self.queries )


## error wrapper
def error( string ):
	sys.stderr.write( string )
	sys.exit( 1 )


## parse input
def parse( input ):
	datasets = []

	it = iter( input )
	n_cases = it.next().strip()
	if not n_cases.isdigit():
		error(  "ERROR parse(): expecting n_cases integer on first line, instead found\n%s\n" % ( n_cases ) )
	n_cases = int( n_cases )
		
	counter = 0 # track number of cases read
	while True:
		try:
			# start of new case, read engines
			n_engines = it.next().strip()
			counter += 1
			ds = DataSet()
			sys.stdout.write( "handling case %d\n" % ( counter ) )

			if not n_engines.isdigit():
				error( "ERROR parse(): expecting n_engines integer, instead found\n%s\n" % ( n_engines ) )
			n_engines = int( n_engines )
			sys.stdout.write( "   expecting %4d engines..." % ( n_engines ) )
			for e in range( n_engines ):
				ds.engines.append( it.next().strip() )
			sys.stdout.write( " read %4d\n" % ( len( ds.engines ) ) )
			if len( ds.engines ) != n_engines:
				error( "ERROR parse(): only %d engines read, should be %d!\n" % ( len( ds.engines ), n_engines ) )

			# read queries
			n_queries = it.next().strip()
			if not n_queries.isdigit():
				error( "ERROR parse(): expecting n_queries integer, instead found\n%s\n" % ( n_queries ) )
			n_queries = int( n_queries )
			sys.stdout.write( "   expecting %4d queries..." % ( n_queries ) )
			for q in range( n_queries ):
				ds.queries.append( it.next().strip() )
			sys.stdout.write( " read %4d\n" % ( len( ds.queries ) ) )
			if len( ds.queries ) != n_queries:
				error( "ERROR parse(): only %d queries read, should be %d!\n" % ( len( ds.queries ), n_queries ) )


			# add to list of datasets
			datasets.append( ds )
		except StopIteration: # end of input 
			break

	# error check
	if counter != n_cases:
		sys.stderr.write( "ERROR parse(): only %d cases found, should be %d!\n" % ( counter, n_cases ) )
		sys.exit( 1 )

	return datasets


## compute optimal switches for a dataset
def optimal_switch( ds ):
	n_engines = ds.n_engines()
	n_queries = ds.n_queries()

	# first convert queries to integers for comparison speed
	engine2id = {}
	for i in range( n_engines ):
		engine2id[ ds.engines [ i ] ] = i
	q = []
	for i in ds.queries:
		q.append( engine2id[ i ] )

	# find optimal number of switches
	switch = 0
	seen = sets.Set()
	for i in q:
		if i not in seen:
			seen.add( i )
		if len( seen ) == n_engines:
			seen.clear()
			switch += 1
			seen.add( i )
	return switch

## main
if __name__ == '__main__':
	usage = "usage: %prog [OPTIONS] input_file" 
	parser = OptionParser( usage, version=0.001 )
	parser.add_option( "-o", "--output", action="store", type="string", dest="output_filename", default=None, help="output filename" )

	( options, args ) = parser.parse_args()
	if len( args ) == 0:
		parser.print_help()
		sys.exit( 1 )
	elif len( args ) < 1:
		error( "need input file" )

	out = sys.stdout
	if options.output_filename != None:
		out = open( options.output_filename, 'w' )

	f = open( args[ 0 ] )
	datasets = parse( f )
	f.close()
	
	print
	for i in range( len( datasets ) ):
		out.write( "Case #%d: %d\n" % ( i+1, optimal_switch( datasets[ i ] ) ) )

	out.close()

