# -*- coding: utf-8 -*-

def run_cases( file_prefix, runner, debug_level ):
    numCases = 0
    
    textReader = open('%s.in'  % (file_prefix,), 'r')
    textWriter = open('%s.out' % (file_prefix,), 'w')
    
    numCases = int( textReader.readline() )
    
    for caseNumber in xrange( 1, numCases + 1 ):
        
        # Note: The number of lines of input (and how to process them)
        #       is up to each individual problem..
        answer = runner( textReader, debug_level )
        
        # Output the results
        textWriter.write('Case #%d: %s\n' % (caseNumber, answer))
        
    textReader.close()
    textWriter.close()

def read_params( infile ):
    line_in = infile.readline()
    params = line_in.strip().split()
    return params

def pause( message="Press ENTER to continue.." ):
    raw_input( message )

def get_simple_options( args, optdict ):
    from optparse import OptionParser

    parser = OptionParser()
    for optname in optdict:
        action = None
        args = [ "-%s" % (optname[0:1],), "--%s" % (optname,) ]
        kwargs = { 'dest': optname, 'default': optdict[optname] }
        if type(optdict[optname]) == bool:
            # TODO: Figure out the right way to do this...
            if optdict[optname] == False:
                kwargs['action'] = 'store_true'
            else:
                kwargs['action'] = 'store_false'
        parser.add_option( *args, **kwargs )

    (options, args) = parser.parse_args()
    return options, args

def interpolate( template_str, params ):
    """ Return the passed template string (using ${var}) filled in with the passed parameters. """
    from string import Template
    template = Template( template_str )
    return template.substitute( params )
